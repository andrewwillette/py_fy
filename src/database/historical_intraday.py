from services.iex import iex
from database.helpers import helpers
from database import crud
from database import models

def saveIntradayDataDay(ticker, date):
    print('date is ')
    print(date)
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

def saveIntradayDataMonth(ticker, month):
    for day in month:
        saveIntradayDataDay(ticker, day)

# def saveIntradayDataYear(ticker, year):
