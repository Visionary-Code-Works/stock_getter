import yfinance as yf
import time
import os

def fetch_current_prices(tickers):
    """Fetches current prices for a list of stock tickers."""
    prices = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        price = stock.info.get('currentPrice', 'N/A')
        prices[ticker] = price
    return prices

def rolling_ticker_display(tickers, interval=10):
    """Displays a rolling ticker of stock prices."""
    try:
        while True:
            prices = fetch_current_prices(tickers)
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
            for ticker, price in prices.items():
                print(f"{ticker}: {price}", end=" | ")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopped the rolling ticker.")

if __name__ == "__main__":
    tickers = [
    # Technology
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB', 'INTC', 'NVDA', 'AMD', 'TSLA', 'ORCL', 'IBM',

    # Finance
    'JPM', 'BAC', 'WFC', 'C', 'GS', 'AXP', 'PYPL', 'SQ',

    # Healthcare
    'JNJ', 'PFE', 'UNH', 'MRK', 'ABBV', 'GILD',

    # Consumer Goods
    'PG', 'KO', 'PEP', 'NKE', 'TGT', 'COST',

    # Energy
    'XOM', 'CVX', 'COP', 'PSX', 'SLB',

    # Telecommunications
    'T', 'VZ', 'TMUS',

    # Industrials
    'GE', 'MMM', 'HON',

    # Materials
    'BHP', 'LIN', 'ECL',

    # Utilities
    'NEE'
]

    rolling_ticker_display(tickers)
