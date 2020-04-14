from config import config
from helpers import logger
from simulations import simulation1
from services.alpaca import alpaca
from services.iex import iex
from datetime import datetime
from services.alpaca.orders import short

#alpaca.sellMarketOrder("AMZN")
# dateToPrint = datetime(2020, 4, 9)
# logger.printToFile(iex.getHistoricalIntradayByMinute("AAPL", dateToPrint), dateToPrint.strftime("%Y-%m-%d") + ".txt")

#intraday_data = iex.getHistoricalIntradayByMinute("AAPL", datetime(2020, 4, 9))
#print(intraday_data)
# simulation1.run()
short.short("PG")
print("hello world")