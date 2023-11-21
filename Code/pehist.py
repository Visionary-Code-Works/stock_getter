import yfinance as yf
import matplotlib.pyplot as plt

# Define a list of tickers
tickers = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB', 'INTC', 'NVDA', 'AMD', 'TSLA', 'ORCL', 'IBM',
    'JPM', 'BAC', 'WFC', 'C', 'GS', 'AXP', 'PYPL', 'SQ', 'JNJ', 'PFE', 'UNH', 'MRK',
    'ABBV', 'GILD', 'PG', 'KO', 'PEP', 'NKE', 'TGT', 'COST', 'XOM', 'CVX', 'COP', 'PSX',
    'SLB', 'T', 'VZ', 'TMUS', 'GE', 'MMM', 'HON', 'BHP', 'LIN', 'ECL', 'NEE'
]

# Fetch data
def fetch_data(metric):
    data = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        value = stock.info.get(metric)
        if value is not None:
            data.append(value)
    return data

# Plot histogram
def plot_histogram(data, metric, bins=30):
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, alpha=0.7)
    plt.title(f'Histogram of {metric} for Selected Stocks')
    plt.xlabel(metric)
    plt.ylabel('Frequency')
    plt.show()

# Metrics to analyze
metrics = ['trailingPE', 'marketCap', 'fiftyTwoWeekChange']

# Generate histograms for each metric
for metric in metrics:
    data = fetch_data(metric)
    plot_histogram(data, metric)
