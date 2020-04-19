from database import historical_intraday
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from helpers import logger

def volumeByMinuteLineGraph(ticker, day):
    minutes_data = historical_intraday.getByTickerAndDay(ticker, day)

    seriesData = {}
    for row in minutes_data:
        seriesData.update({ pd.to_datetime(row.intraday_data.get('minute')) : row.intraday_data.get('volume')})
    volumeByMinuteSeries = pd.Series(seriesData)
    graph = volumeByMinuteSeries.plot.line()
    graph.set_xlabel("Time (in minutes)")
    graph.set_ylabel("Volume")
    logger.writeGraphToFile(graph.get_figure(), "_".join([ticker, day.strftime("%Y-%m-%d"), "volumeGraph"]))

def priceByMinuteLineGraph(ticker, day):
    minutes_data = historical_intraday.getByTickerAndDay(ticker, day)

    seriesData = {}
    for row in minutes_data:
        seriesData.update({ pd.to_datetime(row.intraday_data.get('minute')) : row.intraday_data.get('average')})
    volumeByMinuteSeries = pd.Series(seriesData)
    graph = volumeByMinuteSeries.plot.line()
    graph.set_xlabel("Time (in minutes)")
    graph.set_ylabel("Average Price")
    logger.writeGraphToFile(graph.get_figure(), "_".join([ticker, day.strftime("%Y-%m-%d"), "priceGraph"]))