import pandas as pd
import json
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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

def calculate_something_similar(portfolio):
    stock_info = get_stocks()
    stock_info['text_for_embedding'] = stock_info['sector'] + ' ' + stock_info['industry']
    stock_info['text_for_embedding'] = stock_info['text_for_embedding'].astype(str)
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(stock_info['text_for_embedding'])
    df_tfidf = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out())
    df_tfidf['isin'] = stock_info['isin']
    # set isin as index
    df_tfidf.set_index('isin', inplace=True)
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    cosine_sim_df = pd.DataFrame(cosine_sim, index=stock_info['isin'], columns=stock_info['isin'])
    np.fill_diagonal(cosine_sim_df.values, np.nan)

    similar_stocks = []
    for stock in portfolio:
        # get top 5 similar stocks, add only isin
        isin = stock['isin']
        selection = cosine_sim_df[isin]
                     
        # check if selection is Series or DataFrame
        if isinstance(selection, pd.DataFrame):
            # select first column
            selection = selection.iloc[:, 0]

        selection = selection.sort_values(ascending=False)

        # drop stocks with similarity of 0.0
        selection = selection[selection > 0.0]
        
        similar_stocks.append(selection)

    # concat with duplicates
    similar_stocks = pd.concat(similar_stocks)

    # remove duplicates
    similar_stocks = similar_stocks.sort_values(ascending=False)
    similar_stocks = similar_stocks[~similar_stocks.index.duplicated(keep='first')]

    similar_stocks = similar_stocks[:3]
    similar_stocks = similar_stocks.reset_index()
    similar_stocks = similar_stocks.to_dict(orient='records')
    similar_stocks = [{'isin': stock['isin']} for stock in similar_stocks]

    return similar_stocks
