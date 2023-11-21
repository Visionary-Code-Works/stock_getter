import yfinance as yf

class StockDataFetcher:
    def __init__(self, ticker):
        """Initialize the stock data fetcher with a specific ticker."""
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)
        
    def get_stock_about(self):
        """Fetches and returns key information about the stock's company."""
        info_keys = ['longName', 'sector', 'industry', 'fullTimeEmployees', 'website', 'city', 'country', 'phone', 'longBusinessSummary']
        about_info = {key: self.stock.info.get(key, 'N/A') for key in info_keys}

        about_str = '\n'.join([f"{key.replace('_', ' ').title()}: {value}" for key, value in about_info.items()])
        return about_str

    # ... other existing methods ...

    def display_all_data(self):
        """Displays all available data for the stock."""
        data_methods = sorted([m for m in dir(self) if m.startswith('get_')])
        for method_name in data_methods:
            method = getattr(self, method_name)
            data = method()
            print(f"{method_name[4:].replace('_', ' ').title()}: {data}")

    def get_avg_daily_volume(self):
        """Fetches and returns the stock's average daily trading volume."""
        avg_volume = self.stock.info.get('averageVolume', 'N/A')
        current_price = self.stock.info.get('currentPrice', 'N/A')
        today_volume = self.stock.info.get('volume', 'N/A')

        # Construct a response string with the fetched data
        response = (f"Average Daily Volume: {avg_volume}\n"
                    f"Current Price: {current_price}\n"
                    f"Today's Volume: {today_volume}\n")
        return response

    def get_book_value(self):
        """Fetches and returns the stock's book value."""
        return self.stock.info.get('bookValue', 'N/A')

    def get_change(self):
        """Fetches and returns the stock's daily price change."""
        return self.stock.info.get('change', 'N/A')

    def get_year_range(self):
        """Fetches and returns the stock's 52-week range."""
        return self.stock.info.get('fiftyTwoWeekRange', 'N/A')

    def display_all_data(self):
        """Displays all available data for the stock."""
        data_methods = sorted([m for m in dir(self) if m.startswith('get_')])
        for method_name in data_methods:
            method = getattr(self, method_name)
            data = method()
            print(f"{method_name[4:].replace('_', ' ').title()}: {data}")

# Example Usage
if __name__ == "__main__":
    ticker = input("Enter a stock ticker (e.g., AAPL, GOOGL): ")
    stock_fetcher = StockDataFetcher(ticker)
    stock_fetcher.display_all_data()
