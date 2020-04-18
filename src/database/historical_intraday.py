from services.iex import iex
from database.helpers import helpers
from database import crud
from database import models
from helpers import time
from sqlalchemy import and_

# saves intraday_data provided from iex api to postgre db
def saveIntradayDataDay(ticker, date):
    intraday_data = iex.getHistoricalIntradayByMinute(ticker, date)
    date_string = helpers.convertDatetimeToString(date)
    s = crud.Session()

    for minute_data in intraday_data:
        historical_intraday = models.Historical_Intraday(
            date=date_string,
            ticker=ticker,
            intraday_data=minute_data
        )
        s.add(historical_intraday)
    s.commit()
    s.close()

def saveIntradayDataMonth(ticker, year, month):
    days = time.getAllDaysOfMonth(2020, 3)
    for day in days:
        saveIntradayDataDay(ticker, day)

def saveIntradayDataYear(ticker, year):
    months = range(1, 12)
    print(months)
    for month in months:
        saveIntradayDataMonth(ticker, year, month)

def getByTickerAndDay(ticker,day):
    s = crud.Session()
    return s.query(models.Historical_Intraday).filter(
        and_(
            models.Historical_Intraday.ticker == ticker,
            models.Historical_Intraday.date == helpers.convertDatetimeToString(day)
        )
        ).all()
