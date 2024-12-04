import sys
import logging
import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import yfinance as yf
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

warnings.filterwarnings("ignore", "use_inf_as_na")

# Suppressing the yfinance errors
logger = logging.getLogger("yfinance")
logger.disabled = True
logger.propagate = False
pd.reset_option("all", silent = True)

class stock_analyzer:
    def __init__(self, master):
        self.master = master
        self.master.title("Stock Analyzer")

        self.period_list = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]

        # Requesting the time period
        tk.Label(master, text = "Enter the time period:").grid(row = 0, column = 0)
        self.period_entry = tk.Entry(master)
        self.period_entry.grid(row = 0, column = 1)

        # Requesting the number of companies
        tk.Label(master, text = "Enter the number of companies that you want to analyze:").grid(row = 1, column = 0)
        self.num_companies_entry = tk.Entry(master)
        self.num_companies_entry.grid(row = 1, column = 1)

        # Requesting the company tickers
        tk.Label(master, text = "Enter Tickers (comma-separated):").grid(row = 2, column = 0)
        self.tickers_entry = tk.Entry(master)
        self.tickers_entry.grid(row = 2, column = 1)

        # Creating the analyze button
        self.analyze_button = tk.Button(master, text = "Analyze", command = self.analyze)
        self.analyze_button.grid(row = 3, column = 0, columnspan = 2)

        # Creating the status message
        self.status_label = tk.Label(master, text = "")
        self.status_label.grid(row = 4, column = 0, columnspan = 2)

    def analyze(self):
        period = self.period_entry.get().strip()
        num_companies = self.num_companies_entry.get().strip()
        tickers = self.tickers_entry.get().strip().split(',')

        if period not in self.period_list:
            messagebox.showerror("Input Error", "Please enter a valid time period.")
            return
        try:
            num_companies = int(num_companies)
            if num_companies < 2 or num_companies > 4:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a number between 2 and 4 for companies.")
            return

        if len(tickers) != num_companies:
            messagebox.showerror("Input Error", "Number of tickers does not match the specified number of companies.")
            return

        self.status_label.config(text = "Fetching data...")
        self.master.update()

        self.company_list = []
        self.historical_data_dict = {}

        for ticker in tickers:
            ticker = ticker.strip().upper()
            try:
                historical_data = yf.Ticker(ticker).history(period = period)
                if historical_data.empty:
                    raise Exception("Empty data")
                self.company_list.append(ticker)
                self.historical_data_dict[ticker] = historical_data
            except Exception as e:
                messagebox.showerror("Error", f"Could not fetch data for {ticker}: {str(e)}")
                return

        self.status_label.config(text = "Data fetched successfully!")
        self.basic_plot_generator()
        self.comparison_plot_generator()

    def basic_plot_generator(self):
        for company in self.company_list:
            historical_data = self.historical_data_dict[company]
            fig, axs = plt.subplots(3, 2, figsize = (19, 9.5))

            axs[0, 0].plot(historical_data["Close"], label = "Closing Price", color = "blue")
            axs[0, 0].set_title(f"Closing Price of {company}", size = 10)
            axs[0, 0].set_xlabel("Date", size = 8)
            axs[0, 0].set_ylabel("Price (USD)", size = 8)

            axs[1, 0].plot(historical_data["Volume"], label = "Sales Volume", color = "blue")
            axs[1, 0].set_title(f"Sales Volume of {company}", size = 10)
            axs[1, 0].set_xlabel("Date", size = 8)
            axs[1, 0].set_ylabel("Volume", size = 8)

            historical_data["Daily Return"] = historical_data["Close"].pct_change()
            axs[2, 0].plot(historical_data["Daily Return"], label = "Daily Return", color = "blue")
            axs[2, 0].set_title(f"Daily Returns of {company}", size = 10)
            axs[2, 0].set_xlabel("Date", size = 8)
            axs[2, 0].set_ylabel("Daily Return (%)", size = 8)

            axs[0, 1].hist(historical_data["Close"], bins = 25, color = "blue")
            axs[0, 1].set_xlabel("Price (USD)", size = 8)
            axs[0, 1].set_ylabel("Counts", size = 8)

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
            axs[1, 1].legend(fontsize=6, loc = "lower right")

            axs[2, 1].hist(historical_data["Daily Return"], bins=25, color="blue")
            axs[2, 1].set_xlabel("Daily Return (%)", size=8)
            axs[2, 1].set_ylabel("Counts", size=8)

            plt.tight_layout()
            plt.show()

    def comparison_plot_generator(self):
        combined_data_1 = pd.DataFrame()
        for company in self.company_list:
            historical_data = self.historical_data_dict[company]
            closing_prices = historical_data[["Close"]].rename(columns = {"Close": company})
            combined_data_1 = combined_data_1.join(closing_prices, how = "outer")
        combined_data_1.reset_index(inplace = True)

        closing_prices_fig = sns.PairGrid(combined_data_1.dropna())
        closing_prices_fig.map_lower(sns.kdeplot, cmap = "winter")
        closing_prices_fig.map_upper(plt.scatter, color = "blue")
        closing_prices_fig.map_diag(plt.hist, bins = 25, color = "blue")
        plt.suptitle("Comparison of Closing Prices", fontsize = 16, y = 1.025)
        plt.show()

        combined_data_2 = pd.DataFrame()
        for company in self.company_list:
            historical_data = self.historical_data_dict[company]
            daily_returns = historical_data[["Daily Return"]].rename(columns = {"Daily Return": company})
            combined_data_2 = combined_data_2.join(daily_returns, how = "outer")
        combined_data_2.reset_index(inplace = True)

        daily_returns_fig = sns.PairGrid(combined_data_2.dropna())
        daily_returns_fig.map_lower(sns.kdeplot, cmap = "winter")
        daily_returns_fig.map_upper(plt.scatter, color = "blue")
        daily_returns_fig.map_diag(plt.hist, bins = 25, color = "blue")
        plt.suptitle("Comparison of Daily Returns", fontsize = 16, y = 1.025)
        plt.show()

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
        plt.scatter(combined_data_2.mean(), combined_data_2.std(), s = area)
        plt.xlabel("Expected Return")
        plt.ylabel("Risk")
        for label, x, y in zip(combined_data_2.columns, combined_data_2.mean(), combined_data_2.std()):
            plt.annotate(label, xy = (x, y), xytext = (50, 50), textcoords = "offset points",
                         ha = "right", va = "bottom", arrowprops = dict(arrowstyle = "-", color = "blue",
                         connectionstyle = "arc3, rad = -0.3"))
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = stock_analyzer(root)
    root.mainloop()
