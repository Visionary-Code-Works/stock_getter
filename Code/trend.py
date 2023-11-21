import yfinance as yf
import pandas as pd

# Load Apple's financial data
aapl = yf.Ticker("AAPL")
income_statement = aapl.financials

# Calculate year-over-year revenue growth
revenue = income_statement.loc['Total Revenue']
revenue_growth = revenue.pct_change() * 100  # Convert to percentage

print("Apple's Year-over-Year Revenue Growth (%):")
print(revenue_growth)
