import pandas as pd
import json
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .raffi_class import dummy_info, build_dummy_investor

"""def get_investor(investor_id):
    name = dummy_info[investor_id][0]
    investor_type = dummy_info[investor_id][1]
    sector_bias = dummy_info[investor_id][2]
    investor_preference = dummy_info[investor_id][3]
    investor = build_dummy_investor(dummy_id=investor_id, dummy_name=name, dummy_investor_type=investor_type, 
                         dummy_sector_bias=sector_bias, dummy_investor_preference=investor_preference)
    return json.loads(investor.generate_json())"""

def get_investor(investor_id):
    file_path = [
        os.path.dirname(__file__),
        "..",
        "..",
        "analysis",
        f"{investor_id}.json"
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

def select_stocks(investor:object):
    """
    Select stocks for the further recommendation process.
    Stocks from sector bias and other large postions.

    Args:
    - investor (object): Object from the class Investor, which contains all info about the investor
   
    Returns:
    - selected_stocks (list): List of selected stocks
    """

    print(f'Selecting stocks for investor {investor["_name"]}\n----------------------------------------------')

    sector_allocation = investor["_sector_allocation"]
    sector_bias = max(sector_allocation, key=sector_allocation.get) # identify sector bias of investor
    print(f'Identified sector bias: {sector_bias}')
    investor_portfolio = investor["_portfolio"]
    bias_portfolio = []
    for position in investor_portfolio:
        if position['sector'] == sector_bias:
            bias_portfolio.append(position) # all positions from the biased sector

    # identify largest postions in the portfolio that are in the biased sector
    sorted_bias_portfolio = sorted(bias_portfolio, key=lambda x: x['portfolio_percent'], reverse=True)
    selected_stocks = []
    number_for_range = min(4, len(sorted_bias_portfolio)) # select 4 stocks from bias, if less exist, pick as many as there are
    for index in range(number_for_range):
        selected_stocks.append(sorted_bias_portfolio[index]['isin'])
    print(f'{selected_stocks}, selected from bias sector\n----------------------------------------------')
    
    # select largest two positions from portfolio, if not already selected
    sorted_portfolio = sorted(investor_portfolio, key=lambda x: x['portfolio_percent'], reverse=True)
    for index in range(2, -1, -1): # loop backwards for correct position in list
        if sorted_portfolio[index]['isin'] not in selected_stocks:
            selected_stocks.insert(1, sorted_portfolio[index]['isin']) # insert at 2nd index of list
            print(sorted_portfolio[index]['isin'], "is a large position but not in bias sector; will be selected as well")
    print(f'All relevant stocks selected!\nFinal selection: {selected_stocks}\n----------------------------------------------')
    return selected_stocks

def calculate_something_similar(investor):
    portfolio = investor["_portfolio"]
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

    selected_stocks = select_stocks(investor)
    print("BANANAS")
    print(selected_stocks)

    similar_stocks = []
    for stock in selected_stocks:
        # get top 5 similar stocks, add only isin
        isin = stock
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

    similar_stocks = similar_stocks[:5]
    similar_stocks = similar_stocks.reset_index()
    similar_stocks = similar_stocks.to_dict(orient='records')
    similar_stocks = [{'isin': stock['isin']} for stock in similar_stocks]

    return similar_stocks
