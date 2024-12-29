from flask import Flask, jsonify, request
from database import db, StockSentimentData
from stock_sentiment import get_summary

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sentiment_data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route("/get-insight", methods=["GET"])
def home_page():
    # get access query params
    new_data = {
        "ticker": request.args.get("ticker"), 
        "from_date": request.args.get("fromDate"), 
        "to_date": request.args.get("toDate")
    }

    # try to get response from api, otherwise, throw bad request
    try:
        summary, score = get_summary(new_data)
        # save data to db
        save_analysis(new_data, summary, score)
    except Exception as e:
        return jsonify({"error": f"{e}"}), 400

    return jsonify({"ticker": new_data["ticker"], "fromDate": new_data["from_date"], "toDate": new_data["to_date"], "summary": summary}), 200

# save new analysis to db
def save_analysis(user_data, summary, score):
    # create sentiment data object
    new_analysis = StockSentimentData(ticker_symbol=user_data["ticker"], from_date=user_data["from_date"], to_date=user_data["to_date"], score=score, summary=summary)

    try:
        db.session.add(new_analysis)
        db.session.commit()
    except Exception as db_error:
        db.session.rollback()
        raise Exception(f"Failed to save analysis to database: {str(db_error)}") from db_error

# main entry point
if __name__ == "__main__":
    app.run(debug=True)
