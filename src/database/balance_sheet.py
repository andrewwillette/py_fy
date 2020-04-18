from services.iex import iex
from database.helpers import helpers
from database import crud
from database import models

def saveBalanceSheet(ticker):
    s = crud.Session()
    
    balance_sheet = models.Balance_Sheet(
            ticker=ticker,
            balance_sheet=iex.getBalanceSheet(ticker)
        )
    
    s.add(balance_sheet)
    s.commit()
    s.close()