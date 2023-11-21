import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the tickers
tickers = ['AAPL', 'GOOGL', 'AMZN']

# Function to fetch revenue and calculate year-over-year growth
def get_revenue_growth(ticker):
    company = yf.Ticker(ticker)
    income_statement = company.financials
    if 'Total Revenue' in income_statement.index:
        revenue = income_statement.loc['Total Revenue']
        revenue_growth = revenue.pct_change(periods=-1)  # Negative periods for yoy growth
        return revenue_growth.dropna().iloc[0]  # Take the most recent growth value
    else:
        return None

# Fetch revenue growth for each company
growth_data = {ticker: get_revenue_growth(ticker) for ticker in tickers}

# Filter out None values if any company data is unavailable
growth_data = {k: v for k, v in growth_data.items() if v is not None}

# Prepare data for pie chart
labels = growth_data.keys()
sizes = [abs(growth) for growth in growth_data.values()]
explode = [0.1 if max(sizes) == size else 0 for size in sizes]  # Explode the max growth slice

# Plotting
plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.title('Year-over-Year Revenue Growth of Tech Giants')
plt.show()
