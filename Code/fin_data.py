import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Helper function to convert market cap and other financials to float
def convert_to_float(value):
    if isinstance(value, str):
        if value[-1] == 'T':  # Trillion
            return float(value[:-1]) * 1e12
        elif value[-1] == 'B':  # Billion
            return float(value[:-1]) * 1e9
        elif value[-1] == 'M':  # Million
            return float(value[:-1]) * 1e6
        elif value[-1] == 'K':  # Thousand
            return float(value[:-1]) * 1e3
        else:  # Just a number in string format
            return float(value)
    elif isinstance(value, (int, float)):  # Already numeric
        return value
    return None  # If value is None or not recognized

# Define the tickers list
tickers = ['AAPL', 'GOOGL', 'AMZN', 'MSFT', 'TSLA', 'FB', 'BRK-A']

# Prepare DataFrame to hold financial data
financial_data = pd.DataFrame()

# Loop over each ticker to retrieve financial information
for ticker in tickers:
    stock = yf.Ticker(ticker)
    info = stock.info
    
    # Extract desired metrics and add them to the DataFrame
    financial_data = financial_data.append({
        'Ticker': ticker,
        'PE Ratio': convert_to_float(info.get('trailingPE')),
        'Market Cap': convert_to_float(info.get('marketCap')),
        'Forward PE': convert_to_float(info.get('forwardPE')),
        'Price to Book': convert_to_float(info.get('priceToBook')),
        'Enterprise to Revenue': convert_to_float(info.get('enterpriseToRevenue')),
        'Profit Margins': convert_to_float(info.get('profitMargins'))
    }, ignore_index=True)

# Drop rows with missing data to keep the DataFrame clean
financial_data.dropna(inplace=True)

# Plot histograms for each metric
for column in financial_data.columns[1:]:  # Skip the 'Ticker' column
    plt.figure(figsize=(10, 5))
    # Check if the data is numeric and not empty
    if pd.to_numeric(financial_data[column], errors='coerce').notnull().all():
        plt.hist(financial_data[column], bins=15, alpha=0.7)
        plt.title(f'Histogram of {column} for Selected Stocks')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()
    else:
        print(f"Skipping histogram for {column} as it contains non-numeric data.")
