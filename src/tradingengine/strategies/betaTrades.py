from services.iex import iex
from helpers.logger import Logger
from services.alpaca.alpaca import Alpaca
import random
import threading

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
                Logger.all('quickTradeOne triggering bracket trade on {} at current price {}, limit '.format(stock, currentPrice, ))
                Logger.debug('making order on stock {}'.format(stock))
                investedStocks += 1
