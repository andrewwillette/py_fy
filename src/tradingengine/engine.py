from services.alpaca import alpaca
from services.iex import iex
from database.persistance import Persistance
from helpers.logger import Logger
from tradingengine.strategies.betaTrades import BetaTrades
import math
import threading
from queue import Queue

class Engine():

    budget = 20000

    def __init__(self, budget):
        self.budget = budget 

    @staticmethod
    def testingThreads(integer):
        while(True):
            print("running thread number {}".format(integer))

    def run(self):
        threadCount = 10
        budgetPerThread = self.budget/threadCount
        stockQueue = Queue()
        for stock in iex.getAllTickers():
            stockQueue.put(stock)
        threads = []
        for i in range(threadCount):
            t = threading.Thread(target=BetaTrades.quickTradeOne, args=[budgetPerThread, stockQueue])
            # t = threading.Thread(target=callme, args=[i])
            threads.append(t)
            t.start()

        Logger.trace('thread count is ')
        Logger.trace(threading.activeCount())
