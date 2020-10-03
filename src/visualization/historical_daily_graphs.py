from database import historical_daily
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from helpers import logger

def openingPriceOverYearLineGraph(ticker, year):
    dailyData = historical_daily.getByTickerAndYear(ticker, year)

    seriesData = {}
    for row in dailyData:
        seriesData.update({ pd.to_datetime(row.date) : row.data.get('open')})
    openingByDaySeries = pd.Series(seriesData)
    graph = openingByDaySeries.plot.line()
    graph.set_xlabel("Day")
    graph.set_ylabel("Opening Price")
    logger.writeGraphToFile(graph.get_figure(), "_".join([ticker, str(year), "Opening Price"]))

def closingPriceOverYearLineGraph(ticker, year):
    dailyData = historical_daily.getByTickerAndYear(ticker, year)

    seriesData = {}
    for row in dailyData:
        seriesData.update({ pd.to_datetime(row.date) : row.data.get('close')})
    openingByDaySeries = pd.Series(seriesData)
    graph = openingByDaySeries.plot.line()
    graph.set_xlabel("Day")
    graph.set_ylabel("Closing Price")
    logger.writeGraphToFile(graph.get_figure(), "_".join([ticker, str(year), "Closing Price"]))

def volumeOverYearLineGraph(ticker, year):
    dailyData = historical_daily.getByTickerAndYear(ticker, year)

    seriesData = {}
    for row in dailyData:
        seriesData.update({ pd.to_datetime(row.date) : row.data.get('volume')})
    openingByDaySeries = pd.Series(seriesData)
    graph = openingByDaySeries.plot.line()
    graph.set_xlabel("Day")
    graph.set_ylabel("Volume")
    logger.writeGraphToFile(graph.get_figure(), "_".join([ticker, str(year), "Volume"]))
