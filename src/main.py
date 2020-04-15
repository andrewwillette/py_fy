from config import config
from helpers import logger
from simulations import simulation1
from services.alpaca import alpaca
from services.iex import iex
from datetime import datetime
from services.alpaca.orders import short
from services.newsapi import newsapi
from database import crud
from database.helpers import helpers
from database import historical_intraday
import calendar

#alpaca.sellMarketOrder("AMZN")
# dateToPrint = datetime(2020, 4, 9)
# logger.printToFile(iex.getHistoricalIntradayByMinute("AAPL", dateToPrint), dateToPrint.strftime("%Y-%m-%d") + ".txt")

#intraday_data = iex.getHistoricalIntradayByMinute("AAPL", datetime(2020, 4, 9))
#print(intraday_data)
# simulation1.run()
# logger.printToFile(iex.testFrameRate("AMD"), "amdSample.txt")
#short.shortTheClose("JPM")

# crud.clearDatabase()
# crud.initializeFromModels()

month = calendar.month(2020,4)
historical_intraday.saveIntradayDataMonth("AMD", month)
# data = iex.getHistoricalIntradayByMinute("AMD", datetime(2020,4,14))
# print('date is ')
# print(datetime(2020,4,14))
# print(data)