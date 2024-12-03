# pip install yfinance
# pip install -U matplotlib

import sys
import logging
import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import yfinance as yf  # For reading stock data from Yahoo
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore", "use_inf_as_na")

# Suppressing the yfinance errors
logger = logging.getLogger("yfinance")
logger.disabled = True
logger.propagate = False

pd.reset_option("all", silent = True)

print("ydsaglme\nCS50’s Introduction to Programming with Python")

def main():
    period_list = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
    while True:
        period = input("Enter the time period: ").strip()
        if period not in period_list:
            print("Something went wrong! Please, enter a valid time period.")
        else:
            break
    # Requesting the period
    data_puller(period)
    basic_plot_generator(company_list)
    comparison_plot_generator(company_list)

def data_puller(period):
    while True:
        try:
            number_of_company = int(input("Enter the number of companies that you want to analyze: ").strip())
            if number_of_company > 4:
                print("Please, enter 4 or less than 4 companies!")
            elif number_of_company < 2:
                print("Please, enter 2 or more than 2 companies!")
            else:
                break
        except ValueError:
            print("Please, enter a valid input!")
            pass
    
    global company_list
    company_list = []
    global historical_data_dict
    historical_data_dict = {}
    
    # Requesting the ticker symbol of companies
    for _ in range(number_of_company):
        while True:
            ticker_symbol = input("Enter the ticker of the company: ").upper()
            if ticker_symbol in company_list:
                print("This element already exists in the list! Please, enter a different element.")
            else:
                try:
                    # Creating the ticker object
                    ticker = yf.Ticker(ticker_symbol)
                    # Extracting data for a specified time period
                    historical_data = ticker.history(period = period)
                    if historical_data.empty:
                        raise Exception
                        break
                    else:
                        company_list.append(ticker_symbol)
                        # Storing data by ticker
                        historical_data_dict[ticker_symbol] = historical_data
                        break
                except:
                    print("Something went wrong! Please, enter a valid ticker.")
    
    print("Companies to analyze:", company_list)

def basic_plot_generator(company_list):
    for company in company_list:
        # Retrieving data for the current ticker
        historical_data = historical_data_dict[company]
        
        fig, axs = plt.subplots(3, 2, figsize = (19, 9.5))

        # Historical view of the closing price in a line graph
        axs[0, 0].plot(historical_data["Close"], label = "Closing Price", color = "blue")
        axs[0, 0].set_title(f"Closing Price of {company}", size = 10)
        axs[0, 0].set_xlabel("Date", size = 8)
        axs[0, 0].set_ylabel("Price (USD)", size = 8)
        axs[0, 0].tick_params(axis = "x", labelsize = 6)
        axs[0, 0].tick_params(axis = "y", labelsize = 6)

        # Historical view of the total volume of stock being traded each day in a line graph
        axs[1, 0].plot(historical_data["Volume"], label = "Sales Volume", color = "blue")
        axs[1, 0].set_title(f"Sales Volume of {company}", size = 10)
        axs[1, 0].set_xlabel("Date", size = 8)
        axs[1, 0].set_ylabel("Volume", size = 8)
        axs[1, 0].tick_params(axis = "x", labelsize = 6)
        axs[1, 0].tick_params(axis = "y", labelsize = 6)

        # Daily return of the stock on average in a line graph
        historical_data["Daily Return"] = historical_data["Close"].pct_change()

        axs[2, 0].plot(historical_data["Daily Return"], label = "Daily Return", color = "blue")
        axs[2, 0].set_title(f"Daily Returns of {company}", size = 10)
        axs[2, 0].set_xlabel("Date", size = 8)
        axs[2, 0].set_ylabel("Daily Return (%)", size = 8)
        axs[2, 0].tick_params(axis = "x", labelsize = 6)
        axs[2, 0].tick_params(axis = "y", labelsize = 6)

        # Historical view of the closing price in a histogram
        axs[0, 1].hist(historical_data["Close"], bins = 25, color = "blue")
        axs[0, 1].set_xlabel("Price (USD)", size = 8)
        axs[0, 1].set_ylabel("Counts", size = 8)
        axs[0, 1].tick_params(axis = "x", labelsize = 6)
        axs[0, 1].tick_params(axis = "y", labelsize = 6)

        # Simple moving average over a specific period of time in a line graph
        sma_days = [10, 20, 30]
        for sma in sma_days:
            historical_data[f"{sma}-day SMA"] = historical_data["Close"].rolling(sma).mean()

        axs[1, 1].plot(historical_data["Close"], label = "Closing Price", color = "blue")
        axs[1, 1].plot(historical_data[f"{sma_days[0]}-day SMA"], label = "10-day SMA", color = "red")
        axs[1, 1].plot(historical_data[f"{sma_days[1]}-day SMA"], label = "20-day SMA", color = "green")
        axs[1, 1].plot(historical_data[f"{sma_days[2]}-day SMA"], label = "30-day SMA", color = "orange")
        axs[1, 1].set_title(f"Closing Price and SMAs for {company}", size = 10)
        axs[1, 1].set_xlabel("Date", size = 8)
        axs[1, 1].set_ylabel("Price (USD)", size = 8)
        axs[1, 1].tick_params(axis = "x", labelsize = 6)
        axs[1, 1].tick_params(axis = "y", labelsize = 6)
        axs[1, 1].legend(fontsize = 6, loc = "lower right")

        # Daily return of the stock on average in a histogram
        axs[2, 1].hist(historical_data["Daily Return"], bins = 25, color = "blue")
        axs[2, 1].set_xlabel("Daily Return (%)", size = 8)
        axs[2, 1].set_ylabel("Counts", size = 8)
        axs[2, 1].tick_params(axis = "x", labelsize = 6)
        axs[2, 1].tick_params(axis = "y", labelsize = 6)

        plt.tight_layout()
        # Displaying the plots
        plt.show()
        
def comparison_plot_generator(company_list):
    # Comparing closing prices of each company
    combined_data_1 = pd.DataFrame()
    for company in company_list:
        historical_data = historical_data_dict[company]
        closing_prices = historical_data[["Close"]].rename(columns = {"Close": company})
        combined_data_1 = combined_data_1.join(closing_prices, how = "outer")
    combined_data_1.reset_index(inplace = True)
    print(combined_data_1)
    
    closing_prices_fig = sns.PairGrid(combined_data_1.dropna())
    closing_prices_fig.map_lower(sns.kdeplot, cmap = "winter")
    closing_prices_fig.map_upper(plt.scatter, color = "blue")
    closing_prices_fig.map_diag(plt.hist, bins = 25, color = "blue")
    plt.suptitle("Comparison of Closing Prices", fontsize = 16, y = 1.025)
    
    # Comparing daily returns of each company
    combined_data_2 = pd.DataFrame()
    for company in company_list:
        historical_data = historical_data_dict[company]
        daily_returns = historical_data[["Daily Return"]].rename(columns = {"Daily Return": company})
        combined_data_2 = combined_data_2.join(daily_returns, how = "outer")
    combined_data_2.reset_index(inplace = True)
    print(combined_data_2)
    
    daily_returns_fig = sns.PairGrid(combined_data_2.dropna())
    daily_returns_fig.map_lower(sns.kdeplot, cmap = "winter")
    daily_returns_fig.map_upper(plt.scatter, color = "blue")
    daily_returns_fig.map_diag(plt.hist, bins = 25, color = "blue")
    plt.suptitle("Comparison of Daily Returns", fontsize = 16, y = 1.025)
    
    # Comparing closing prices and daily returns of each company with heatmap
    combined_data_1 = combined_data_1.drop("Date", axis = 1)
    combined_data_2 = combined_data_2.drop("Date", axis = 1)
    plt.figure(figsize = (9.5, 9.5))
    plt.subplot(2, 2, 1)
    sns.heatmap(combined_data_1.corr(), annot = True, cmap = "winter")
    plt.title("Correlation of Closing Prices")
    
    plt.subplot(2, 2, 2)
    sns.heatmap(combined_data_2.corr(), annot = True, cmap = "winter")
    plt.title("Correlation of Daily Returns")
    
    combined_data_2 = combined_data_2.dropna()
    area = np.pi * 20
    plt.figure(figsize = (9.5, 9.5))
    plt.scatter(combined_data_2.mean(), combined_data_2.std(), s = area) # "s" indicates the marker size
    plt.xlabel("Expected Return")
    plt.ylabel("Risk")
    for label, x, y in zip(combined_data_2.columns, combined_data_2.mean(), combined_data_2.std()):
        # Adding annotations to relevant plot
        plt.annotate(label, xy = (x, y), xytext = (50, 50), textcoords = "offset points", ha = "right", va = "bottom", arrowprops = dict(arrowstyle = "-", color = "blue", connectionstyle = "arc3, rad = -0.3"))

if __name__ == "__main__":
    main()