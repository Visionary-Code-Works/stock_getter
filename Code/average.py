"""This module fetches and displays moving averages and average trading volume for a given stock ticker."""
import yfinance as yf
import pandas as pd

class StockAveragesFetcher:
    def __init__(self, ticker):
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)
        self.data = self.stock.history(period="1y")  # Fetching 1 year of historical data

    def get_moving_averages(self, window_sizes=[20, 50, 200]):
        """Calculate and return moving averages for specified window sizes."""
        moving_averages = {}
        for window in window_sizes:
            ma = self.data['Close'].rolling(window=window).mean()
            moving_averages[f'{window}-day MA'] = ma[-1]  # Get the latest moving average
        return moving_averages

    def get_average_volume(self):
        """Return the average trading volume."""
        return self.data['Volume'].mean()

    def display_all_averages(self):
        """Display all calculated averages."""
        print(f"--- Averages for {self.ticker} ---")
        ma = self.get_moving_averages()
        for key, value in ma.items():
            print(f"{key}: {value:.2f}")

        avg_volume = self.get_average_volume()
        print(f"Average Volume: {avg_volume:.2f}")

# Example Usage
ticker = input("Enter a stock ticker (e.g., AAPL, GOOGL): ")
averages_fetcher = StockAveragesFetcher(ticker)
averages_fetcher.display_all_averages()
