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
        return "<Historical_Intraday(date='{}', intraday_by_minute={})>"\
                .format(self.date, self.intraday_by_minute)