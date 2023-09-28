from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

@app.route("/")
def home():
    path = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_csv(path + "/../../data/stock_info.tsv", sep="\t")
    return jsonify(df.to_dict(orient="records"))
