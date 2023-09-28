import yfinance as yf
import pandas as pd
import numpy as np
import os

path = os.path.dirname(os.path.abspath(__file__))

def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    historical_data = stock.history(period="1y")
    historical_data['Daily Return'] = historical_data['Close'].pct_change()
    historical_data['Daily Return'].dropna(inplace=True)
    volatility = np.std(historical_data['Daily Return'])
    annual_volatility = volatility * np.sqrt(252)
    info['Volatility'] = volatility
    info['Annual Volatility'] = annual_volatility
    return info

def get_stock_list():
    stock_list = pd.read_csv(path + "/../data/stock_list.csv")
    return stock_list

if __name__ == "__main__":
    # print number of stocks in the list
    stock_list = get_stock_list()
    print("Number of stocks in the list: {}".format(len(stock_list)))

    # get stock info for each stock in the list
    stock_info_list = []
    # loop through each stock in the dataframe
    for index, row in stock_list.iterrows():
        ticker = row["ISIN"]
        stock_info = get_stock_info(ticker)
        stock_info_list.append(stock_info)
        print("Stock info for {} is done.".format(ticker))

    # convert list of dictionaries to dataframe
    stock_info_df = pd.DataFrame(stock_info_list)
    stock_info_df.to_csv(path + "/../data/stock_info.csv", index=False)
    print("Stocks info is saved to data/stock_info.csv")

