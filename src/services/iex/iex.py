from iexfinance.stocks import Stock, get_historical_intraday
import os
from datetime import datetime, timedelta
from iexfinance.refdata import get_iex_symbols

def getQuote(ticker):
    return Stock(ticker).get_quote()

def getStockDifferenceFromWeekAgo(ticker):
    one_week = datetime.timedelta(days=7)
    right_now = datetime.datetime.now()
    one_week_ago = right_now - one_week
    currentStock = Stock(ticker, token=auth_token)
    oldStock = get_historical_data(ticker, one_week_ago, close_only=True)
    # not finished, need to find value of current and old from json object and subtract

# prints stock quote price continuously so to witness the update rate
def testFrameRate(ticker):
    while True:
        print("current time is " + datetime.now().strftime("%H %M %S %f"))
        print(Stock(ticker).get_price())

def getHistoricalIntradayByMinute(ticker, day):
    return get_historical_intraday(ticker, day)

def getCurrentPrice(ticker):
    return Stock(ticker).get_price()

def getBalanceSheet(ticker):
    return Stock(ticker).get_balance_sheet()

def getAllTickers():
    return get_iex_symbols()