import os
from dotenv import load_dotenv
import re
import requests
import pandas as pd
from eodhd import APIClient
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import matplotlib.pyplot as plt

load_dotenv()
EODHD_API_KEY = os.getenv("eodhd_api_key")
OPENAI_API_KEY = os.getenv("openai_api_key")

# allow for data exchange from eodhd
api = APIClient(EODHD_API_KEY)

# get news for apple for example (100 results between 1st and 31st of October 2024)
data = api.financial_news(
  s='AAPL.US', 
  from_date='2024-10-01', 
  to_date='2024-10-31', 
  limit=100
)

# url = f'https://eodhd.com/api/eod/AAPL.US?api_token={EODHD_API_KEY}&fmt=json'
# response = requests.get(url).json()
# print(response)

# set up dataframe (JSON --> dataframe)
df = pd.DataFrame(data)
df.tail()

print(df)

##### HELPER FUNCTIONS #######################################################################
def clean_text(text):
  cleaned_text = re.sub(r'\s+', ' ', text)
  return cleaned_text.strip()

def count_tokens(text):
  tokens = text.split()
  return len(tokens)
##############################################################################################

# clean text in dataframe
df['content'] = df['content'].apply(clean_text)

# form llm chain with openai mode using langchain
model = ChatOpenAI(
  model='gpt-3.5-turbo', 
  openai_api_key = OPENAI_API_KEY, 
  temperature=0
)

print(f'\n==========================TEST 1==========================\n')

# set up template to construct an optimized prompt 
template = """
Identify the sentiment towards the Apple(AAPL) stocks from the news article , where the sentiment score should be from -10 to +10 where -10 being the most negative and +10 being the most positve , and 0 being neutral

Also give the proper explanation for your answers and how would it effect the prices of different stocks

Article : {statement}
"""

# form proper prompt for model
prompt = PromptTemplate(template=template, input_variables=['statement'])
# set up llm chain
chain = prompt | model

# demo response
print(chain.invoke(df['content'][13]).content)
print(f'\n==========================TEST 2==========================\n')

# apply token count to dataframe
df['TokenCount'] = df['content'].apply(count_tokens)
# define token count threshold
token_count_threshold = 3500
# create new dataframe filtering based on token count
new_df = df[df['TokenCount'] < token_count_threshold]
# drop token count column from new dataframe if unused
new_df = new_df.drop('TokenCount', axis=1)
# reset index
new_df=new_df.reset_index(drop=True)

# set up more concise template
template_2 = """
Identify the sentiment towards the Apple(AAPL) stocks of the news article from -10 to +10 where -10 being the most negative and +10 being the most positve , and 0 being neutral

GIVE ANSWER IN ONLY ONE WORD AND THAT SHOULD BE THE SCORE

Article : {statement}
"""

# forming prompt using Langchain PromptTemplate functionality
prompt_2 = PromptTemplate(template=template_2, input_variables=["statement"])
# set up new chain for prompt 2
chain_2 = prompt_2 | model

# demo one inference
print(new_df['content'][2])
print('')
print('News sentiment: ', chain_2.invoke(new_df['content'][2]).content)

# fill list with sentiments
sentiments = []
for i in range(0, new_df.shape[0]):
  sentiments.append(chain_2.invoke(new_df['content'][i]).content)

# convert list to dataframe
sentiments_df = pd.DataFrame(sentiments)
# remove all zeros
sentiments_df = sentiments_df[sentiments_df[0] != '0']
# get counts of each value (i.e. counts of -5, -3, +7, etc)
counts = sentiments_df[0].value_counts()

# plot data using pie chart
plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
plt.title('AAPL.US Sentiments')
plt.axis('equal')
# show the plot
plt.show()