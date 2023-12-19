from flask import Flask, jsonify, url_for, make_response, request, jsonify
from flask_cors import CORS
import backend.api.lib as lib
import requests
import pandas as pd

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
        if pd.isna(row["longBusinessSummary"]):
            x["description"] = ""
        else:
            x["description"] = row["longBusinessSummary"]

        if pd.isna(row["beta"]):
            x["beta"] = 0
        else:
            x["beta"] = row["beta"]

        if pd.isna(row["dividendYield"]):
            x["dividend"] = 0
        else:
            x["dividend"] = row["dividendYield"]

        # check for NaN in trailingPE
        if pd.isna(row["trailingPE"]):
            x["trailingPE"] = 0
        else:
            x["trailingPE"] = row["trailingPE"]

        if pd.isna(row["52WeekChange"]):
            x["52WeekChange"] = 0
        else:
            x["52WeekChange"] = row["52WeekChange"]
            
        return x
    
    # @todo, calculate something similar with cron job
    investor = lib.get_investor(investor_id)
    portfolio = investor["_portfolio"]
    data["something_similar"] = lib.calculate_something_similar(investor)
    data["something_similar"] = list(map(mapper, data["something_similar"]))
    data["something_essential"] = list(map(mapper, investor["_something_essential"]))
    data["something_special"] = list(map(mapper, investor["_something_similar_beta"]))
    return jsonify(data)

@app.route("/stocks/")
def get_stocks():
    data = lib.get_stocks()
    return jsonify(data.to_dict(orient="records"))

@app.route("/engage", methods=["POST"])
def engage():
    data = request.get_json()
    print(data)
    # send json request to http://34.41.133.178:8777/
    r = requests.post("http://34.41.133.178:8777/engage", json=data)
    return jsonify({"status": "success", "message": "Data saved successfully."})
