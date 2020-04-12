from iexfinance.stocks import Stock
import os

iex_auth_token = os.environ["IEXAuthToken"]

def getAppleQuote():
    apple_stock = Stock("AAPL", token=iex_auth_token)
    return apple_stock.get_quote()

def getAppleBalanceSheet():
    apple_stock = Stock("AAPL", token=iex_auth_token)
    return apple_stock.get_balance_sheet()

def getAppleCashFlow():
    apple_stock = Stock("AAPL", token=iex_auth_token)
    return apple_stock.get_cash_flow()
