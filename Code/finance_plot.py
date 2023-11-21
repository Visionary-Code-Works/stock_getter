"""plotting.py: Plot historical stock data for a list of companies."""
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta

# Define the tickers of the companies you're interested in
tickers = ['AAPL', 'GOOGL', 'AMZN',
            'MSFT', 'META', 'TSLA',
            'NVDA', 'PYPL', 'ADBE']

# Set the start and end dates for the data. Here, we're looking at the last year.
today = date.today()
end_date = today.strftime("%Y-%m-%d")  # Today's date in YYYY-MM-DD format
start_date = (today - timedelta(days=360)).strftime("%Y-%m-%d")  # Date one year ago

# Fetch historical stock data for each ticker using yfinance's download function
all_data = {ticker: yf.download(ticker, start=start_date, end=end_date, progress=False) for ticker in tickers}

# Function to plot historical closing prices of a stock
def plot_closing_prices(data, title):
    """Plot the closing prices of a stock.

    Args:
    data (DataFrame): The historical data of the stock.
    title (str): The title of the plot.
    """
    data['Close'].plot(title=title)  # Plot the closing prices
    plt.xlabel('Date')  # Label for the x-axis
    plt.ylabel('Closing Price')  # Label for the y-axis
    plt.show()  # Display the plot

# Function to plot moving averages along with the closing prices
def plot_moving_averages(data, title, window_sizes=[20, 50]):
    """Plot moving averages along with closing prices for a stock.

    Args:
    data (DataFrame): The historical data of the stock.
    title (str): The title of the plot.
    window_sizes (list): List of integers representing the window sizes for moving averages.
    """
    plt.figure(figsize=(10, 6))  # Set the size of the plot
    plt.plot(data['Close'], label='Closing Prices', alpha=0.5)  # Plot closing prices
    # Plot each moving average
    for window in window_sizes:
        plt.plot(data['Close'].rolling(window=window).mean(), label=f'{window}-Day MA')
    plt.title(title)  # Set the title of the plot
    plt.xlabel('Date')  # Label for the x-axis
    plt.ylabel('Price')  # Label for the y-axis
    plt.legend()  # Display the legend
    plt.show()  # Show the plot

# Iterate over each stock and plot its data
for ticker, data in all_data.items():
    plot_closing_prices(data, f"{ticker} Closing Prices")  # Plot closing prices
    plot_moving_averages(data, f"{ticker} Moving Averages")  # Plot moving averages
