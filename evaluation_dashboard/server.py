from flask import Flask, jsonify, url_for, make_response, render_template, request, jsonify
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
import pandas as pd
import threading
import os

app = Flask(__name__)
CORS(app)

csv_file_path = 'metrics.csv'

csv_file_lock = threading.Lock()

if not os.path.exists(csv_file_path):
    df = pd.DataFrame(columns=['user', 'recommender', 'action', 'stock', 'timestamp'])
    df.to_csv(csv_file_path, index=False)

auth = HTTPBasicAuth()

USERNAME = "CIO"
PASSWORD = "RecommenderModul2023"

@auth.verify_password
def verify_password(username, password):
    if username == USERNAME and password == PASSWORD:
        return True
    return False

@app.route("/")
@auth.login_required
def home():

    # read csv file
    df = pd.read_csv(csv_file_path)

    essential_df = df[df['recommender'] == 'essential']
    alpha_df = df[df['recommender'] == 'alpha']
    beta_df = df[df['recommender'] == 'beta']

    essential_like_ratio = "N/A"
    essential_dislike_ratio = "N/A"
    alpha_like_ratio = "N/A"
    alpha_dislike_ratio = "N/A"
    beta_like_ratio = "N/A"
    beta_dislike_ratio = "N/A"

    if len(essential_df) > 0:
        essential_like_ratio = len(essential_df[essential_df['action'] == 'like']) / len(essential_df)
        essential_dislike_ratio = len(essential_df[essential_df['action'] == 'dislike']) / len(essential_df)
        # convert to percentage
        essential_like_ratio = "{:.2%}".format(essential_like_ratio)
        essential_dislike_ratio = "{:.2%}".format(essential_dislike_ratio)
    
    if len(alpha_df) > 0:
        alpha_like_ratio = len(alpha_df[alpha_df['action'] == 'like']) / len(alpha_df)
        alpha_dislike_ratio = len(alpha_df[alpha_df['action'] == 'dislike']) / len(alpha_df)
        # convert to percentage
        alpha_like_ratio = "{:.2%}".format(alpha_like_ratio)
        alpha_dislike_ratio = "{:.2%}".format(alpha_dislike_ratio)

    if len(beta_df) > 0:
        beta_like_ratio = len(beta_df[beta_df['action'] == 'like']) / len(beta_df)
        beta_dislike_ratio = len(beta_df[beta_df['action'] == 'dislike']) / len(beta_df)
        # convert to percentage
        beta_like_ratio = "{:.2%}".format(beta_like_ratio)
        beta_dislike_ratio = "{:.2%}".format(beta_dislike_ratio)

    return render_template(
        "index.html",
        essential_like_ratio=essential_like_ratio,
        essential_dislike_ratio=essential_dislike_ratio,
        alpha_like_ratio=alpha_like_ratio,
        alpha_dislike_ratio=alpha_dislike_ratio,
        beta_like_ratio=beta_like_ratio,
        beta_dislike_ratio=beta_dislike_ratio
    )

def save_to_csv(data):
    with csv_file_lock:
        df = pd.read_csv(csv_file_path)
        df = pd.concat([df, pd.DataFrame(data, index=[0])], ignore_index=True)
        df.to_csv(csv_file_path, index=False)

@app.route('/engage', methods=['POST'])
def engage():
    try:
        data = request.get_json()
        save_to_csv(data)
        return jsonify({'status': 'success', 'message': 'Data saved successfully.'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8777)