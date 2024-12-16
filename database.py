from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

# set up SQLite and base class for ORM
engine = create_engine("sqlite:///stock_data.db")
db = sessionmaker(bind=engine)

Base = declarative_base()

class StockSentimentData(Base):
    __tablename__ = "stock sentiment data"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticker_symbol = db.Column(db.String(14), nullable=False)
    from_date = db.Column(db.DateTime, nullable=False, default=datetime.now(datetime.timezone.utc))
    to_date = db.Column(db.DateTime, nullable=False, default=datetime.now(datetime.timezone.utc))
    sentiment_score = db.Column(db.Integer, nullable=False)
    summary = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"""
        <StockSentimentData(
            ticker_symbol={self.ticker_symbol}, 
            from_date={self.from_date}, 
            to_date={self.to_date}, 
            sentiment_score={self.sentiment_score}, 
            summary={self.summary}
        )>
        """