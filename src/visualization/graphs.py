from services.iex import iex
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from helpers.logger import Logger

def byMinuteIntradayLineGraph(ticker, yaxis, day=None):
    minutes_data = iex.getHistoricalIntradayByMinute(ticker, day)
    seriesData = {}
    for row in minutes_data:
        seriesData.update({ pd.to_datetime(row.get('minute')) : row.get(yaxis)})
    try:
        volumeByMinuteSeries = pd.Series(seriesData)
        graph = volumeByMinuteSeries.plot.line()
        graph.set_xlabel("Time (in minutes)")
        graph.set_ylabel(yaxis)
        if(day==None):
            day = datetime.today()
        Logger.writeGraphToFile(graph.get_figure(), "_".join([ticker, day.strftime("%Y-%m-%d"), yaxis, "graph"]))
    except Exception as ex:
        print("error generating graph for ticker:{}, yaxis:{}".format(ticker, yaxis))
        print (ex)

def valueOverRangeLineGraph(ticker, value, start, end):
    dailyData = iex.getHistoricalDataByRange(ticker, start, end)
    print('here1, should log iex historvatl range')
    Logger.debug('iex historical range data is')
    Logger.debug(dailyData)
    seriesData = {}
    for day, value in dailyData.items():
        print('day is')
        print(day)
        print(value)
        seriesData.update({ pd.to_datetime(day) : value.get('close')})
    openingByDaySeries = pd.Series(seriesData)
    graph = openingByDaySeries.plot.line()
    graph.set_xlabel("Day")
    graph.set_ylabel(value)
    Logger.writeGraphToFile(graph.get_figure(), "_".join([ticker, str(start), str(end), "Closing Price"]))

def closingPriceOverYearLineGraph(ticker, year):
    dailyData = historical_daily.getByTickerAndYear(ticker, year)

    seriesData = {}
    for row in dailyData:
        seriesData.update({ pd.to_datetime(row.date) : row.data.get('close')})
    openingByDaySeries = pd.Series(seriesData)
    graph = openingByDaySeries.plot.line()
    graph.set_xlabel("Day")
    graph.set_ylabel("Closing Price")
    Logger.writeGraphToFile(graph.get_figure(), "_".join([ticker, str(year), "Closing Price"]))

def volumeOverYearLineGraph(ticker, year):
    dailyData = historical_daily.getByTickerAndYear(ticker, year)

    seriesData = {}
    for row in dailyData:
        seriesData.update({ pd.to_datetime(row.date) : row.data.get('volume')})
    openingByDaySeries = pd.Series(seriesData)
    graph = openingByDaySeries.plot.line()
    graph.set_xlabel("Day")
    graph.set_ylabel("Volume")
    Logger.writeGraphToFile(graph.get_figure(), "_".join([ticker, str(year), "Volume"]))