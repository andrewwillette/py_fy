from helpers import logger, time
from config import config
from services.iex import iex
from datetime import datetime
from visualization import graphs 
import calendar
import sys
import dateparser
import argparse

parser = argparse.ArgumentParser(description='Process financial information.')
parser.add_argument('ticker', help='The stock symbol to analyze.')
parser.add_argument('-gp', '--graphprice', metavar='date_range', dest='price_dates', nargs='*', help='Generate a graph for the stock price in the given dates')
parser.add_argument('-gv', '--graphvolume', metavar='date_range', dest='volume_dates', nargs='*', help='Generate a graph for the stock volume in the given dates')
parser.add_argument('-t', '--trade', action='store_true', help='Actively trade on the Alpaca paper market with rules specified in trading libraries.')
parser.add_argument('-fv', '--findvalue', action='store_true', help='Scan stock information for interesting investments')
args = parser.parse_args()

print('parsed args is')
print(args)

ticker = args.ticker

# TODO: Make ticker optional so trade and findvalue can be called without it
if(args.ticker):
    try:
        quote = iex.getQuote(ticker)
    except Exception as ex:
        print("Provided Ticker {} is not a valid symbol.".format(ticker))
        sys.exit()
    print('Current Price: {}'.format(quote.get('latestPrice')))
    print('PE Ratio: {}'.format(quote.get('peRatio')))
    print('52-Week High: {}'.format(quote.get('week52High')))
    print('52-Week Low: {}'.format(quote.get('week52Low')))
    logger.writeToLog(iex.getQuote(args.ticker))

if(args.price_dates):
    print('graphprice args is')
    print(args.graphprice)
    parsedDate = dateparser.parse(args.graphprice)
    if (parsedDate.weekday() < 5):
        graphs.byMinuteIntradayLineGraph(ticker, 'average', parsedDate)
    else:
        print('Provided date is not a weekday, the day was: ' + parsedDate.strftime('%A'))

if(args.volume_dates):
    print('volume_dates len args is')
    print(len(args.volume_dates))
    if(len(args.volume_dates) > 1):
        print("passed multiple volume dates")
        parsedStartDate = dateparser.parse(args.volume_dates[0])
        parsedEndDate = dateparser.parse(args.volume_dates[1])
        graphs.valueOverRangeLineGraph(ticker, 'volume', parsedStartDate, parsedEndDate)
    else:
        print("passed single volume date")
        parsedDate = dateparser.parse(args.volume_dates[0]) 
        if (parsedDate.weekday() < 5):
            graphs.byMinuteIntradayLineGraph(ticker, 'volume', parsedDate)
        else:
            print('Provided date is not a weekday, the day was: ' + parsedDate.strftime('%A'))

if(args.trade):
    print('trading...')
