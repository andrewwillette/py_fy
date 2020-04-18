from database import historical_intraday
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from helpers import logger

def volumeByMinuteHistogram(ticker, day):
    minutes_data = historical_intraday.getByTickerAndDay(ticker, day)
    logger.writeToFile(minutes_data, "minutes-data.txt")

    minutes_indexer = []
    volume_indexer = []
    mydict = {}
    for row in minutes_data:
        mydict.update({ pd.to_datetime(row.intraday_data.get('minute')) : row.intraday_data.get('volume')})
    volumeByMinuteSeries = pd.Series(mydict)
    graph = volumeByMinuteSeries.plot.line()
    graph.set_xlabel("Time (in minutes)")
    graph.set_ylabel("Volume")
    logger.writeGraphToFile(graph.get_figure(), "_".join([ticker, day.strftime("%Y-%m-%d"), "volumeGraph"]))
