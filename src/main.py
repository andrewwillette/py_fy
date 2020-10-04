from config import config
from helpers import logger, time
from simulations import simulation1
from services.alpaca import alpaca
from services.iex import iex
from datetime import datetime
from services.alpaca.orders import short
from services.newsapi import newsapi
from database import crud
from database.helpers import helpers
from database import historical_intraday, balance_sheet, historical_daily, iex_ticker
from visualization import historical_intraday_graphs, historical_daily_graphs
import calendar
import sys
import dateparser
import argparse
#TODO: Parse ticker arg and check if valid ticker

parser = argparse.ArgumentParser(description='Process financial information')
parser.add_argument('ticker', help="The stock symbol to analyze.")
parser.add_argument('--graphdaily', help="Generate a graph for the stock on the given day")
parser.add_argument('--currentprice', action='store_true', help="Get the current price of the stock")
args = parser.parse_args()

if(args.graphdaily):
    parsedDate = dateparser.parse(args.graphdaily)
    if (parsedDate.weekday() < 5):
        historical_intraday_graphs.priceByMinuteLineGraph(args.ticker, parsedDate)
    else:
        print("Provided date is not a weekday, the day was: " + parsedDate.strftime("%A"))

if(args.currentprice):
    print(iex.getCurrentPrice(args.ticker))
    print('got current price')

