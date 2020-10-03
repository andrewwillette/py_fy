from services.iex import iex
from database import crud
from database import models

def saveAllIexTickers():
    tickers = iex.get_iex_symbols()
    s = crud.Session()
    for ticker in tickers:
        print('ticker is')
        print(ticker)
        iex_ticker = models.IexTicker(
            ticker=ticker.get('symbol')
        )
        s.add(iex_ticker)
    s.commit()
    s.close()

