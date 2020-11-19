import sys
import os
os.environ['KIVY_NO_ARGS'] = str(1)
from config import config
import pydevd_pycharm
from helpers.logger import Logger
from services.iex import iex
from services.alpaca.alpaca import Alpaca
from database import crud
from visualization import graphs
from tradingengine.engine import Engine
# from frontend import initialize
import dateparser
import argparse

parser = argparse.ArgumentParser(description='Process financial information')
parser.add_argument('-s', '--symbol', help='The stock symbol to analyze')
parser.add_argument('-gp', '--graphprice', metavar='date_range', dest='price_dates', nargs='*', help='Generate a graph for the stock price in the given dates')
parser.add_argument('-gv', '--graphvolume', metavar='date_range', dest='volume_dates', nargs='*', help='Generate a graph for the stock volume in the given dates')
parser.add_argument('-t', '--trade', action='store_true', help='Actively trade on the Alpaca paper market with rules specified in trading libraries')
parser.add_argument('-fv', '--findvalue', action='store_true', help='Scan stock information for interesting investments')
parser.add_argument('-lp', '--listpositions', action='store_true', help='Output positions of current orders in force')
parser.add_argument('-v', '--verbosity', action='count', default=0, help='Adjust verbosity of the program')
parser.add_argument('-d', '--debug', action='store_true', default=0, help='Activate debugger, must have listener on port 8000')
args = parser.parse_args()

os.environ['log_level'] = str(args.verbosity)

debuggerPort = 8000

if args.debug:
    try:
        pydevd_pycharm.settrace('localhost', port=debuggerPort, stdoutToServer=True, stderrToServer=True)
    except Exception:
        print("Must turn debugger on at port {}. See https://www.jetbrains.com/help/idea/remote-debugging-with-product.html#remote-debug-config".format(debuggerPort))
        sys.exit()

# initialize.PyfyApp().run()
print("does this run now?")
if args.symbol:
    symbol = args.symbol
    Logger.trace("Symbol passed in: {}".format(args.symbol))
    quote = iex.getQuote(symbol)
    Logger.trace("Queried Symbol Quote is ...")
    Logger.trace(quote)
    if(quote != None):
        Logger.info('Current Price: {}'.format(quote.get('latestPrice')))
        Logger.info('PE Ratio: {}'.format(quote.get('peRatio')))
        Logger.info('52-Week High: {}'.format(quote.get('week52High')))
        Logger.info('52-Week Low: {}'.format(quote.get('week52Low')))
    else:
        Logger.error('Could not print symbol information for {}'.format(symbol))

if args.price_dates:
    parsedDate = dateparser.parse(args.graphprice)
    if (parsedDate.weekday() < 5):
        graphs.byMinuteIntradayLineGraph(symbol, 'average', parsedDate)
    else:
        Logger.all('Provided date is not a weekday, the day was: ' + parsedDate.strftime('%A'))

if args.volume_dates:
    if(len(args.volume_dates) > 1):
        parsedStartDate = dateparser.parse(args.volume_dates[0])
        parsedEndDate = dateparser.parse(args.volume_dates[1])
        graphs.valueOverRangeLineGraph(symbol, 'volume', parsedStartDate, parsedEndDate)
    else:
        parsedDate = dateparser.parse(args.volume_dates[0]) 
        if (parsedDate.weekday() < 5):
            graphs.byMinuteIntradayLineGraph(symbol, 'volume', parsedDate)
        else:
            Logger.all('Provided date is not a weekday, the day was: ' + parsedDate.strftime('%A'))

if args.listpositions:
    for position in Alpaca.listPositions():
        Logger.all(position)

if args.trade:
    totalToTrade = 20000
    # tickerquote = Alpaca.getTickerPrice("TSLA")
    engine = Engine(totalToTrade)
    engine.run()

if args.findvalue:
    Logger.info('finding value...')
