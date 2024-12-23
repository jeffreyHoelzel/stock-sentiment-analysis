from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from database import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sentiment_data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.app_context():
    db.create_all()

mar = Marshmallow(app)

class StockSentimentDataSchema(mar.Schema):
    class Meta:
        fields = ("id", "ticker_symbol", "from_date", "to_date", "score", "summary")

one_stock_sentiment_schema = StockSentimentDataSchema()
many_stock_sentiment_schemas = StockSentimentDataSchema(many=True)

@app.route("/get", methods=["GET"])
def home_page():
    return jsonify({"text": "Hello, world!"})

# main entry point
if __name__ == "__main__":
    app.run(debug=True)