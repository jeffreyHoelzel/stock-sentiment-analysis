from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class StockSentimentData(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticker_symbol = db.Column(db.String(14), nullable=False)
    from_date = db.Column(db.Date, nullable=False)
    to_date = db.Column(db.Date, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    summary = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"""
        <StockSentimentData(
            ticker_symbol={self.ticker_symbol}, 
            from_date={self.from_date}, 
            to_date={self.to_date}, 
            score={self.score}, 
            summary={self.summary}
        )>
        """
