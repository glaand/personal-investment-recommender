import pandas as pd
import json
import os
def get_investor(investor_id):
    file_path = [
        os.path.dirname(__file__),
        "..",
        "..",
        "data",
        "dummy_portfolio.json"
    ]
    data = json.load(open(os.path.join(*file_path)))
    return data

def get_recommendation(investor_id):
    file_path = [
        os.path.dirname(__file__),
        "..",
        "..",
        "data",
        "dummy_recommendations.json"
    ]
    data = json.load(open(os.path.join(*file_path)))
    # filter by investor_id and return json object
    filtered_data = [d for d in data if d["investor_id"] == investor_id][0]
    return filtered_data

def get_stocks():
    file_path = [
        os.path.dirname(__file__),
        "..",
        "..",
        "data",
        "stock_info.tsv"
    ]
    data = pd.read_csv(os.path.join(*file_path), sep="\t")
    return data