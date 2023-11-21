import yfinance as yf
import matplotlib.pyplot as plt

# Example 1: Plotting the closing price of a stock
ticker_symbol = 'GOOGL'
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period='1mo')  # Get the last month of data

# Plotting the closing prices
plt.figure(figsize=(10, 6))
plt.plot(ticker_df['Close'], label='GOOGL Close Price')
plt.title('GOOGL Closing Price - Last Month')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)
plt.show()

# Example 2: Plotting volume of stock traded
plt.figure(figsize=(10, 6))
plt.bar(ticker_df.index, ticker_df['Volume'], label='GOOGL Volume', color='orange')
plt.title('GOOGL Trading Volume - Last Month')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.grid(True)
plt.show()

# Example 3: Plotting a histogram of daily price changes in percentage
daily_returns = ticker_df['Close'].pct_change().dropna() * 100  # Calculate daily returns in %

plt.figure(figsize=(10, 6))
plt.hist(daily_returns, bins=50, alpha=0.75, color='purple')
plt.title('Histogram of GOOGL Daily Price Changes')
plt.xlabel('Daily Price Change (%)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
