import yfinance as yf

# Define the tickers
tickers = ['AAPL', 'GOOGL', 'AMZN']

# Function to print financial statements
def print_financial_statements(ticker):
    company = yf.Ticker(ticker)
    
    print(f"--- {ticker} Financial Statements ---")
    
    # Income Statement
    print("\nIncome Statement:")
    print(company.financials)

    # Balance Sheet
    print("\nBalance Sheet:")
    print(company.balance_sheet)

    # Cash Flow
    print("\nCash Flow Statement:")
    print(company.cashflow)

# Get and print financial data for each company
for ticker in tickers:
    print_financial_statements(ticker)
    print("\n" + "-"*50 + "\n")
