import yfinance as yf
import matplotlib.pyplot as plt

def fetch_and_plot(ticker_symbol):
    try:
        # Fetch historical data
        ticker_data = yf.Ticker(ticker_symbol)
        hist_data = ticker_data.history(period='1y')

        # Check if data is empty
        if hist_data.empty:
            raise ValueError("No data found for the given ticker.")

        # Calculate Fibonacci Retracement Levels based on the max and min price in the period
        max_price = hist_data['High'].max()
        min_price = hist_data['Low'].min()
        diff = max_price - min_price
        level1 = max_price - 0.236 * diff
        level2 = max_price - 0.382 * diff
        level3 = max_price - 0.618 * diff

        # Plot the data along with Fibonacci Levels
        plt.figure(figsize=(12, 8))
        plt.plot(hist_data['Close'], label='Close Price')
        plt.axhline(max_price, linestyle='--', alpha=0.5, color='red', label='Max Price')
        plt.axhline(min_price, linestyle='--', alpha=0.5, color='green', label='Min Price')
        plt.axhline(level1, linestyle='--', alpha=0.5, color='orange', label='Fibonacci Level 0.236')
        plt.axhline(level2, linestyle='--', alpha=0.5, color='blue', label='Fibonacci Level 0.382')
        plt.axhline(level3, linestyle='--', alpha=0.5, color='purple', label='Fibonacci Level 0.618')
        plt.title(f'{ticker_symbol} - Fibonacci Retracement Levels')
        plt.xlabel('Date')
        plt.ylabel('Price ($)')
        plt.legend()
        plt.grid(True)
        plt.show()

    except ValueError as ve:
        print(ve)

# User input for ticker symbol
ticker_symbol = input("Enter the stock ticker for analysis (e.g., AAPL): ")
fetch_and_plot(ticker_symbol)

