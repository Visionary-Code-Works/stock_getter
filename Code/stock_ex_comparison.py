import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# List of stock exchanges
# These are not direct ticker symbols but rather ETFs or indices that represent the exchanges
exchanges_list = {
    "^GSPC": "S&P 500",
    "^IXIC": "NASDAQ Composite",
    "^DJI": "Dow Jones Industrial Average",
    "^FTSE": "FTSE 100"  # London Stock Exchange
    # Add more exchanges or indices if needed
}

# User selects 4 exchanges for comparison
selected_exchanges = ["^GSPC", "^IXIC", "^DJI", "^FTSE"]

# Define the time period for analysis
start_date = '2000-01-01'
end_date = '2023-11-01'

# Create an empty DataFrame to store the normalized closing prices
normalized_closing_prices = pd.DataFrame()

# Fetch the closing prices for each exchange
for exchange in selected_exchanges:
    data = yf.download(exchange, start=start_date, end=end_date, progress=False)
    # Normalize the closing prices to compare the performance starting from the same point
    normalized_closing_prices[exchanges_list[exchange]] = data['Close'] / data['Close'].iloc[0]

# Plot the normalized closing prices for comparison
normalized_closing_prices.plot(figsize=(14, 7))
plt.title('Comparative Analysis of Stock Exchange Performance')
plt.xlabel('Date')
plt.ylabel('Normalized Closing Price')
plt.legend(title='Exchange')
plt.grid(True)
plt.show()
