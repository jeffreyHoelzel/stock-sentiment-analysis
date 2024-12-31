from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
from database import db, StockSentimentData
from stock_sentiment import get_summary

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sentiment_data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.app_context():
    db.create_all()

########################################################################################
### Routes
########################################################################################

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

    return jsonify({
        "ticker": new_data["ticker"], 
        "fromDate": new_data["from_date"], 
        "toDate": new_data["to_date"], 
        "summary": summary
    }), 200


########################################################################################
### DB Operations
########################################################################################

# save new analysis to db
def save_analysis(user_data, summary, score):
    # set up date objects before storing to db
    from_date_obj = datetime.strptime(user_data["from_date"], "%Y-%m-%d").date()
    to_date_obj = datetime.strptime(user_data["to_date"], "%Y-%m-%d").date()

    # create sentiment data object
    new_analysis = StockSentimentData(
        ticker_symbol=user_data["ticker"], 
        from_date=from_date_obj, 
        to_date=to_date_obj, 
        score=score, 
        summary=summary)

    try:
        db.session.add(new_analysis)
        db.session.commit()
    except Exception as db_error:
        db.session.rollback()
        print(f"Failed to save analysis to database: {str(db_error)}")
        raise

# main entry point
if __name__ == "__main__":
    app.run(debug=True)
