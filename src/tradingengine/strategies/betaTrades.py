import math
from queue import Queue

from helpers.logger import Logger
from services.alpaca.alpaca import Alpaca
from services.iex import iex


class BetaTrades:
    @staticmethod
    def isIncreasingConsecutively(symbol, iexHistoricalData, repeats):
        Logger.debug('analyzing {} for {} repeated increasing minutes'.format(symbol, repeats))
        chainLength = 0
        failedChains = 0
        beLessThanMeChainHead = None
        for i in range(len(iexHistoricalData) - 1, -1, -1):
            minuteData = iexHistoricalData[i]
            currentMinuteAverage = minuteData.get('average')

            #many trading minutes have no activity
            if(currentMinuteAverage != None):
                if(beLessThanMeChainHead == None):
                    beLessThanMeChainHead = currentMinuteAverage
                elif (currentMinuteAverage < beLessThanMeChainHead):
                    Logger.debug('increasing consecutive count')
                    chainLength += 1
                elif (currentMinuteAverage >= beLessThanMeChainHead):
                    chainLength = 0
                    failedChains += 1
                if(chainLength >= repeats):
                    Logger.debug('successful increasing successfully check on {} for {} repeats'.format(symbol, repeats))
                    return True
                if(failedChains >= 3):
                    Logger.debug('aborting consecutive analysis of {}'.format(symbol))
                    return False
                beLessThanMeChainHead = currentMinuteAverage
        return False

    @staticmethod
    def quickTradeOne(totalToSpend, stockQueue):
        Logger.debug('Calling quickTradeOne with totalToSpend : {}'.format(totalToSpend))
        spent = 0
        investedStocks = 0
        # while (spent < totalToSpend):
        while(spent < totalToSpend):
            stock = stockQueue.get().get('symbol')
            byMinuteData = iex.getHistoricalIntradayByMinute(stock)
            if(BetaTrades.isIncreasingConsecutively(stock, byMinuteData, 8)):
                #make bracket order
                askprice = Alpaca.getAskPrice(stock)
                take_price = askprice * 1.02
                stop_price = askprice * .988
                quantity = math.floor(totalToSpend/askprice)
                Alpaca.buyMarketBracketOrder(stock, take_price, stop_price, quantity)
                Logger.all('quickTradeOne triggering bracket trade on {} at ask price {}, take price {}, stop price {}'.format(stock, askprice, take_price, stop_price))
                investedStocks += 1


    '''
    Scans iex, finds stocks that are both overvalues and falling and opens short positions on them
    TODO: Define different types of short positions
    '''
    @staticmethod
    def shortTheDying(totalToSpend):
        symbolsToShort = ["CERN"]
        # get all stocks
        stockQueue = Queue()
        for stock in iex.getAllTickers():
            stockQueue.put(stock)


        # so now we have queue of all stocks... we want to find most promising short...

        #trades.shortOrder()
