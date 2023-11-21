import yfinance as yf
import matplotlib.pyplot as plt

# Define the top 10 companies by market cap as of 2023 (this list can change over time)
top_10_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'BRK-A', 'META', 'AMD', 'PYPL', 'X','BTC-USD']

# Initialize dictionary to store dataframes for each ticker
historical_data = {}

# Fetch historical data for each of the top 10 tickers
for ticker in top_10_tickers:
    historical_data[ticker] = yf.Ticker(ticker).history(period='1mo')

# Plotting the closing prices for each of the top 10 companies
for ticker, data in historical_data.items():
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label=f'{ticker} Close Price')
    plt.title(f'{ticker} Closing Price - Last Month')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.grid(True)
    plt.show()  # This will display the plot

    # Plotting the volume of stock traded for each of the top 10 companies
    plt.figure(figsize=(10, 6))
    plt.bar(data.index, data['Volume'], label=f'{ticker} Volume', color='orange')
    plt.title(f'{ticker} Trading Volume - Last Month')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.legend()
    plt.grid(True)
    plt.show()  # This will display the plot

    # Plotting a histogram of daily price changes in percentage for each of the top 10 companies
    daily_returns = data['Close'].pct_change().dropna() * 100  # Calculate daily returns in %
    plt.figure(figsize=(10, 6))
    plt.hist(daily_returns, bins=50, alpha=0.75, color='purple')
    plt.title(f'Histogram of {ticker} Daily Price Changes')
    plt.xlabel('Daily Price Change (%)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()  # This will display the plot

