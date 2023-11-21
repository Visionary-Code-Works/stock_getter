# stock_getter

Stock Market Data Analysis Tool
This tool provides various functionalities for analyzing stock market data, including comparative analysis, volatility measurement, Fibonacci retracement levels, and more. It utilizes the yfinance library to fetch historical data from Yahoo Finance and matplotlib for data visualization.

Features
Comparative Analysis: Compares performance of selected stocks or stock indices over a specified period. Users can input stock tickers for a customized comparison.

Volatility Measurement: Calculates and visualizes the 30-day rolling volatility (annualized) of selected stocks.

Fibonacci Retracement: Plots Fibonacci retracement levels for a given stock over the past year. The tool also includes error handling for incorrect or non-existent stock tickers.

Installation
To use this tool, ensure you have Python installed on your system along with the following libraries:
```
bash

pip install yfinance
pip install matplotlib
pip install pandas

```
Comparative Analysis:

Run the script and input 2-3 stock tickers when prompted.
The script will display a comparison of the selected stocks’ normalized closing prices over time.
Volatility Measurement:

The script calculates and plots the rolling volatility of specified stocks.
Users can modify the list of tickers in the script to analyze different stocks.
Fibonacci Retracement:

Enter the desired stock ticker when prompted.
The script will plot the stock's closing prices along with key Fibonacci levels.
Customization

The scripts are customizable, allowing users to specify different stock tickers and time periods for analysis.
Error Handling
The Fibonacci retracement tool includes error handling to manage incorrect user inputs or data unavailability.
Limitations

Due to the nature of financial APIs and data availability, some tickers or indices might not have data accessible through yfinance.
Note

This tool is intended for educational and informational purposes. It should not be considered as financial advice.
