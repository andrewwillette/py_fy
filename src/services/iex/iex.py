from iexfinance.stocks import Stock, get_historical_intraday, get_historical_data
import os
from datetime import datetime, timedelta
from iexfinance.refdata import get_iex_symbols

def getQuote(ticker):
    return Stock(ticker).get_quote()

def getHistoricalDataByYear(ticker, year):
    start = datetime(year, 1, 1)
    end = datetime((year+1), 1, 1)
    return get_historical_data(ticker, start, end)

def getHistoricalDataByRange(ticker, start, end):
    return get_historical_data(ticker, start, end)

def getHistoricalIntradayByMinute(ticker, day=None):
    return get_historical_intraday(ticker, day)

def getCurrentPrice(ticker):
    return Stock(ticker).get_price()

def getBalanceSheet(ticker):
    return Stock(ticker).get_balance_sheet()

def getAllTickers():
    return get_iex_symbols()

# prints stock quote price continuously so to witness the update rate
def testFrameRate(ticker):
    while True:
        print("current time is " + datetime.now().strftime("%H %M %S %f"))
        print(Stock(ticker).get_price())