import sys
import yfinance as yf

# Small script to display todays stock info for followed stocks

# ANSI color codes
RED = '\033[0;31m'
GREEN = '\033[0;32m'
NC = '\033[0m' 

USA_EMOJI = "\U0001F1FA\U0001F1F8"
CANADA_EMOJI = "\U0001F1E8\U0001F1E6"


def fetch_and_display_stock_data(stock_symbols):    
    for stock_symbol in stock_symbols:
        stock = yf.Ticker(stock_symbol)
        data = stock.history(period='2d')

        close_yesterday = data.iloc[-2]['Close']
        close_today = data.iloc[-1]['Close']
        percentage_change = (close_today - close_yesterday) / close_yesterday * 100
        color = GREEN if percentage_change >= 0 else RED
        sign = '+' if percentage_change >= 0 else ''
        flag = CANADA_EMOJI if ".to" in stock_symbol.lower() else USA_EMOJI
        formatted_data = f"{flag} {stock_symbol}: {color}{sign}{percentage_change:.2f}%{NC}"
        print(formatted_data)
 
if __name__ == "__main__":
    stock_symbols = sys.argv[1:]
    fetch_and_display_stock_data(stock_symbols)