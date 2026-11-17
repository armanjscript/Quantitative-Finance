import warnings
import numpy as np
import yfinance as yf
from scipy.stats import norm
import pandas as pd
import datetime

# Silence the inplace warnings coming from inside yfinance on pandas >= 3.1
warnings.filterwarnings("ignore", message=".*The inplace keyword.*")


def download_data(stock, start_date, end_date):
    data = {}
    ticker = yf.Ticker(stock)
    data[stock] = ticker.history(start=start_date, end=end_date, auto_adjust=False)['Adj Close']
    return pd.DataFrame(data)




# This is how we calculate the VaR tomorrow (n=1)
def calculate_var(position, c, mu, sigma):
    v = norm.ppf(1-c)
    VaR = position * (mu - sigma * v)  
    return VaR  


# This is how we calculate the VaR for any days in the future
def calculate_var_n(position, c, mu, sigma, n):
    VaR = position * (mu * n - sigma * np.sqrt(n) * norm.ppf(1-c))
    return VaR 




if __name__ == "__main__":
    start = datetime.datetime(2014, 1, 1)
    end = datetime.datetime(2026, 1, 1)

    stock_data = download_data('C', start, end)
    
    stock_data['returns'] = np.log(stock_data['C'] / stock_data['C'].shift(1))
    stock_data = stock_data[1:]
    
    #This is the investment ($1000000 stock or whatever)
    S = 1e6
    
    # Confidence level - this time it is 95%
    c = 0.95
    
    # We assume that daily returns are normally distributed
    mu = np.mean(stock_data['returns'])
    sigma = np.std(stock_data['returns'])
    
    print('Value at risk is: $%0.2f' % calculate_var(S, c, mu, sigma))
    print('Value at risk is: $%0.2f' % calculate_var_n(S, c, mu, sigma, 10)) #For 10 days

    
    

    