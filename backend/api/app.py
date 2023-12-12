from flask import Flask, jsonify, url_for, make_response
from flask_cors import CORS
import backend.api.lib as lib

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/investors/<investor_id>")
def get_investor(investor_id):
    data = lib.get_investor(investor_id)
    stocks_data = lib.get_stocks()
    def mapper(x):
        row = stocks_data[stocks_data["isin"] == x].iloc[0]
        x = {}
        x["isin"] = row["isin"]
        x["name"] = row["longName"]
        x["description"] = row["longBusinessSummary"]
        return x
    
    print("BANANAS")
    print(data["_bulk_risks"])

    data["_bulk_risks"] = list(map(mapper, data["_bulk_risks"]))
    data["_sell_stocks"] = list(map(mapper, data["_sell_stocks"]))
    data["_high_beta_stocks"] = list(map(mapper, data["_high_beta_stocks"]))
    return jsonify(data)

@app.route("/recommendations/<investor_id>")
def get_recommendation(investor_id):
    data = lib.get_recommendation(investor_id)
    stocks_data = lib.get_stocks()
    def mapper(x):
        row = stocks_data[stocks_data["isin"] == x["isin"]].iloc[0]
        x["name"] = row["longName"]
        x["description"] = row["longBusinessSummary"]
        return x
    
    # @todo, calculate something similar with cron job
    portfolio = lib.get_investor(investor_id)["_portfolio"]
    data["something_similar"] = lib.calculate_something_similar(portfolio)

    data["something_similar"] = list(map(mapper, data["something_similar"]))
    data["something_essential"] = list(map(mapper, data["something_essential"]))
    data["something_special"] = list(map(mapper, data["something_special"]))
    return jsonify(data)

@app.route("/stocks/")
def get_stocks():
    data = lib.get_stocks()
    return jsonify(data.to_dict(orient="records"))