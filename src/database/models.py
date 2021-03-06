from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, JSON

Base = declarative_base()

class Orders(Base):
    __tablename__ = 'Orders'
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    alpacaId = Column(String)
    orderType = Column(String) 
    orderData = Column(JSON)
    orderStatus = Column(String)
    
    def __repr__(self):
        return "<Order(symbol='{}', alpacaId='{}', orderType='{}', orderData='{}', orderStatus='{}')>"\
                .format(self.symbol, self.alpacaId, self.orderType, self.orderData, self.orderStatus)

class Historical_Intraday(Base):
    __tablename__ = 'Historical_Intraday'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    ticker = Column(String)
    intraday_data = Column(JSON)
    
    def __repr__(self):
        return "<Historical_Intraday(date='{}', ticker='{}', intraday_data={})>"\
                .format(self.date, self.ticker, self.intraday_data)

class Historical_Daily(Base):
    __tablename__ = 'Historical_Daily'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    ticker = Column(String)
    data = Column(JSON)
    
    def __repr__(self):
        return "<Historical_Daily(date='{}', ticker='{}', data={})>"\
                .format(self.date, self.ticker, self.data)

class Balance_Sheet(Base):
    __tablename__ = 'Balance_Sheet'
    id = Column(Integer, primary_key=True)
    ticker = Column(String)
    balance_sheet = Column(JSON)
    
    def __repr__(self):
        return "<Balance_Sheet(ticker='{}', balance_sheet={})>"\
                .format(self.ticker, self.balance_sheet)

class IexTicker(Base):
    __tablename__ = 'Iex_Ticker'
    ticker = Column(String, primary_key=True)
    
    def __repr__(self):
        return "<Iex_Ticker(ticker='{}')>"\
                .format(self.ticker)