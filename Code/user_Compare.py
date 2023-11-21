import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Ask the user for stock tickers to compare
user_input = input("Enter max 3 stock tickers to compare, separated by a space: ")
tickers = user_input.split()

# Define the time period for analysis
start_date = '2022-01-01'
end_date = '2023-11-19'

# Create an empty DataFrame to store the normalized closing prices
normalized_closing_prices = pd.DataFrame()

# Fetch the closing prices for each stock
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date, progress=False)
    # Normalize the closing prices to compare the performance starting from the same point
    normalized_closing_prices[ticker] = data['Close'] / data['Close'].iloc[0]

# Plot the normalized closing prices for comparison
normalized_closing_prices.plot(figsize=(14, 7))
plt.title('Comparative Analysis of Stock Performance')
plt.xlabel('Date')
plt.ylabel('Normalized Closing Price')
plt.legend(title='Ticker')
plt.grid(True)
plt.show()
