from services.iex import iex
from helpers.logger import Logger
import random
import threading


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
# scan iex for stocks which have increased today 
def getGoodStocks(totalToSpend, stockQueue):
    spent = 0
    investedStocks = 0
    # while (spent < totalToSpend):
    while(investedStocks < 3):
        stock = stockQueue.get().get('symbol')
        byMinuteData = iex.getHistoricalIntradayByMinute(stock)
        if(isIncreasingConsecutively(stock, byMinuteData, 8)):
            #make bracket order
            Logger.debug('making order on stock {}'.format(stock))
            investedStocks += 1
