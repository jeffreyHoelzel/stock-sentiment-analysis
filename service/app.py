from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from database import db
from stock_sentiment import get_summary

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

@app.route("/get-insight", methods=["GET"])
def home_page():
    # get access query params
    new_data = {
        "ticker": request.args.get("ticker"), 
        "from_date": request.args.get("fromDate"), 
        "to_date": request.args.get("toDate")
    }

    print(new_data)

    try:
        response = get_summary(new_data)
    except Exception as e:
        return jsonify({"error": f"{e}"}), 400

    return jsonify({"ticker": new_data["ticker"], "fromDate": new_data["from_date"], "toDate": new_data["to_date"], "summary": response}), 200

# main entry point
if __name__ == "__main__":
    app.run(debug=True)