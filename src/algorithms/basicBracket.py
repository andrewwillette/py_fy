from services.iex import iex
from services.alpaca import alpaca

def safeBracketOrder(ticker):
  #get current quote. order make bracket order with limit === %1 up and .5% down
    quote_price = iex.getCurrentPrice(ticker)
    take_lim = quote_price * 1.01
    stop_lim = quote_price * .995
    alpaca.buyMarketBracketOrder(ticker, take_lim, stop_lim, 100)
