from services.iex import iex
from database.helpers import helpers
from database import crud
from database import models
from helpers import time
from sqlalchemy import and_
from datetime import datetime

def saveHistoricalDailyByYear(ticker, year):
    dailyData = iex.getHistoricalDataByYear(ticker, 2018)
    s = crud.Session()
    for day, data in dailyData.items():
        historical_daily = models.Historical_Daily(
            date=day,
            ticker=ticker,
            data=data
        )
        s.add(historical_daily)
    s.commit()
    s.close()

def getByTickerAndDay(ticker,day):
    s = crud.Session()
    return s.query(models.Historical_Daily).filter(
        and_(
            models.Historical_Daily.ticker == ticker,
            models.Historical_Daily.date == helpers.convertDatetimeToString(day)
        )
        ).all()

def getByTickerAndYear(ticker,year):
    s = crud.Session()
    return s.query(models.Historical_Daily).filter(
        and_(
            models.Historical_Daily.ticker == ticker,
            models.Historical_Daily.date.like("%" + str(year) + "%")
        )
        ).all()