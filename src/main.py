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

#TODO: Parse ticker arg and check if valid ticker

if("--current" in sys.argv):
    print(iex.getCurrentPrice(sys.argv[1]))
if("--graph-daily" in sys.argv):
    historical_intraday_graphs.priceByMinuteLineGraph(sys.argv[1]) 
if("--graph-monthly" in sys.argv):
    historical_daily_graphs.closingPriceOverYearLineGraph()
#alpaca.sellMarketOrder("AMZN")
# dateToPrint = datetime(2020, 4, 9)
# logger.printToFile(iex.getHistoricalIntradayByMinute("AAPL", dateToPrint), dateToPrint.strftime("%Y-%m-%d") + ".txt")

#intraday_data = iex.getHistoricalIntradayByMinute("AAPL", datetime(2020, 4, 9))
#print(intraday_data)
# simulation1.run()
# logger.printToFile(iex.testFrameRate("AMD"), "amdSample.txt")
#short.shortTheClose("JPM")

#historical_intraday.saveIntradayDataYear("AMD", 2019)
#crud.initializeFromModels()
# balance_sheet.saveBalanceSheet("AMD")
# if __name__ == "__main__":
    # execute only if run as a script
# historical_intraday.saveIntradayDataDay("AMD", datetime(2020, 4, 17))
# historical_intraday_graphs.priceByMinuteLineGraph("AMD", datetime(2020, 4, 17))
#iex_ticker.saveAllIexTickers()

# data = iex.getHistoricalIntradayByMinute("AMD", datetime(2020,4,14))
# print('date is ')
# print(datetime(2020,4,14))
# print(data)
