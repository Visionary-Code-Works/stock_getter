import yfinance as yf
import matplotlib.pyplot as plt

class StockAverageVolumeFetcher:
    def __init__(self, tickers):
        """Initialize the fetcher with a list of stock tickers."""
        self.tickers = tickers
        self.volumes = self.get_average_volumes()

    def get_average_volumes(self):
        """Fetches and returns the average trading volumes for the given tickers."""
        avg_volumes = {}
        for ticker in self.tickers:
            stock = yf.Ticker(ticker)
            history = stock.history(period="1y")
            avg_volumes[ticker] = history['Volume'].mean()
        return avg_volumes

    def plot_average_volumes(self):
        """Plots a pie chart of the average trading volumes."""
        labels = self.volumes.keys()
        sizes = self.volumes.values()

        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title('Average Trading Volume Comparison')
        plt.show()

# Example Usage
tickers = ['AAPL', 'GOOGL',
           'AMZN', 'AMD',
           'DASH', 'SQ',
           'MU', 'SNAP',
           'PYPL', 'ADBE',
          ]  # Add more tickers as needed
volume_fetcher = StockAverageVolumeFetcher(tickers)
volume_fetcher.plot_average_volumes()
