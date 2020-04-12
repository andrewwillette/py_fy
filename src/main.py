from datetime import datetime, timedelta
from helpers import helpers
from config import config
import os
from iexfinance.stocks import Stock, get_historical_data
from services.iex import iex

def getAppleQuote():
    apple_stock = Stock("AAPL", token=auth_token)
    return apple_stock.get_quote()

def getAppleBalanceSheet():
    apple_stock = Stock("AAPL", token=auth_token)
    return apple_stock.get_balance_sheet()

def getAppleCashFlow():
    apple_stock = Stock("AAPL", token=auth_token)
    return apple_stock.get_cash_flow()

def getStockDifferenceFromWeekAgo(ticker):
    one_week = datetime.timedelta(days=7)
    right_now = datetime.datetime.now()
    one_week_ago = right_now - one_week
    currentStock = Stock(ticker, token=auth_token)
    oldStock = get_historical_data(ticker, one_week_ago, close_only=True)
    print(currentStock)
    print(oldStock)

iex_auth_token = os.environ["IEXAuthToken"]
print()
helpers.printToFile(iex.getAppleQuote())