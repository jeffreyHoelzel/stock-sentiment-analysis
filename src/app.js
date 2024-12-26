document.addEventListener("DOMContentLoaded", () => {
  // get html elements for data retrieval, transfer, and formatting on page
  const tickerSymbolInput = document.getElementById("ticker-symbol-input");
  const fromDateInput = document.getElementById("from-date-input");
  const toDateInput = document.getElementById("to-date-input");
  const formBody = document.getElementById("form-body");
  const submitButton = document.getElementById("submit-data");
  const results = document.getElementById("results");

  // function to fetch response from backend giving stock insight
  const getStockInsight = async (data) => {
    try {
      const response = await fetch(`http://localhost:5000/get-insight?${data}`, {
        method: "GET"
      });

      if (!response.ok) {
        throw new Error(`Server responsed with status code: ${response.status}`)
        // handle insertion of error to html
      }

      // if status is 200 (ok), get data in json format
      const stockInsightData = await response.json();

      // display data to user
      results.innerHTML += `
        <div class="results-container">
          <h2 class="ticker-header">${stockInsightData.ticker}</h2>
          <p class="dates"><strong>From:</strong> ${stockInsightData.fromDate}, <strong>To:</strong> ${stockInsightData.toDate}</p>
          <p class="summary"><strong>Summary:</strong> ${stockInsightData.summary}</p>
        </div>
      `;
    } catch (error) {
      console.log(`Error occured while fetching data: ${error}`);
      // handle insertion of fatal error into html
    }
  }

  // listen for form button clicks
  submitButton.addEventListener("click", (e) => {
    // set up stock object and encode as url search param
    const stockQueryData = {
      ticker: tickerSymbolInput.value, 
      fromDate: fromDateInput.value, 
      toDate: toDateInput.value
    };

    const stockQueryParams = new URLSearchParams(stockQueryData).toString();

    console.log(stockQueryData);

    e.preventDefault();
    getStockInsight(stockQueryParams);
    formBody.reset()
  });
});