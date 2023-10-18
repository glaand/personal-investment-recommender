from flask import Flask, jsonify, url_for
import pandas as pd
import json
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/investors/<investor_id>")
def get_investor(investor_id):
    file_path = [
        os.path.dirname(__file__),
        "..",
        "..",
        "data",
        "dummy_portfolio.json"
    ]
    data = json.load(open(os.path.join(*file_path)))
    return jsonify(data)

@app.route("/recommendations/<investor_id>")
def get_recommendation(investor_id):
    file_path = [
        os.path.dirname(__file__),
        "..",
        "..",
        "data",
        "dummy_recommendations.json"
    ]
    data = json.load(open(os.path.join(*file_path)))
    return jsonify(data)