from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, JSON

Base = declarative_base()

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