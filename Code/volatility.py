import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Define the tickers for the analysis
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']

# Define the time period for analysis
start_date = '2007-01-01'
end_date = '2023-01-01'

# Create an empty DataFrame to store the closing prices
closing_prices = pd.DataFrame()

# Fetch the closing prices for each stock
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date, progress=False)
    closing_prices[ticker] = data['Close']

# Calculate the daily returns
daily_returns = closing_prices.pct_change()

# Calculate the rolling standard deviation (volatility)
rolling_volatility = daily_returns.rolling(window=30).std() * (252 ** 0.5)  # Annualized Volatility

# Plotting the rolling volatility
plt.figure(figsize=(15, 8))
for ticker in tickers:
    plt.plot(rolling_volatility[ticker], label=ticker)

plt.title('30-Day Rolling Volatility (Annualized)')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.legend()
plt.grid(True)
plt.show()
