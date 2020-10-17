from services.alpaca import alpaca
from services.iex import iex
from helpers.logger import Logger
from tradingengine.strategies import betaTrades
import math
import threading
from queue import Queue

def callme(int):
    while True:
        print('hello thread' + str(int))

def run():
    TOTAL_TO_SPEND = 30000
    MAX_STOCK_TO_BUY = 500

    stockQueue = Queue()
    for stock in iex.getAllTickers():
        stockQueue.put(stock)
    # betaTrades.getGoodStocks(TOTAL_TO_SPEND)
    threads = []
    for i in range(5):
        t = threading.Thread(target=betaTrades.getGoodStocks, args=[TOTAL_TO_SPEND, stockQueue])
        # t = threading.Thread(target=callme, args=[i])
        threads.append(t)
        t.start()

    Logger.trace('thread count is ')
    Logger.trace(threading.activeCount())
    