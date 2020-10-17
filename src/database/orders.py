from database import crud
from database import models

def saveOrder(symbol, alpacaOrderId):
    s = crud.Session()
    for ticker in tickers:
        order = models.Order(
            
        )
        s.add(order)
    s.commit()
    s.close()
