import yfinance as yf

class StockSummaryFetcher:
    def __init__(self, tickers):
        """ Initialize with a list of stock tickers. """
        self.tickers = tickers if isinstance(tickers, list) else [tickers]
        self.summaries = [self.fetch_summary(ticker) for ticker in self.tickers]

    def fetch_summary(self, ticker):
        """ Fetches a summary of the stock. """
        stock = yf.Ticker(ticker)
        info = stock.info
        return {
            'Name': info.get('longName'),
            'Sector': info.get('sector'),
            'Industry': info.get('industry'),
            'Country': info.get('country'),
            'Exchange': info.get('exchange'),
            'Website': info.get('website'),
            'Summary': info.get('longBusinessSummary'),
            'Currency': info.get('currency'),
            'Quote Type': info.get('quoteType'),
            'Market': info.get('market'),
            'Ticker': ticker,
            'Previous Close': info.get('previousClose'),
            'Day Range': info.get('regularMarketDayRange'),
            '52 Week Range': info.get('fiftyTwoWeekRange'),
            'Market Cap': info.get('marketCap'),
            'Average Volume': info.get('averageVolume'),
            'P/E Ratio': info.get('trailingPE')
            
        }

    def display_summary(self):
        """ Displays the summary information for each stock. """
        for summary in self.summaries:
            print(f"\nSummary for {summary['Ticker']}:\n")
            for key, value in summary.items():
                print(f"{key}: {value if value is not None else 'N/A'}")

def main():
    tickers = input("Enter stock ticker(s) separated by commas (e.g., GOOGL, AAPL): ").split(',')
    fetcher = StockSummaryFetcher([ticker.strip() for ticker in tickers])
    fetcher.display_summary()

if __name__ == "__main__":
    main()
