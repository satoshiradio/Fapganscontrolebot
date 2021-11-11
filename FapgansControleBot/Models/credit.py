import datetime

from sqlalchemy import Column, Integer, DateTime

from FapgansControleBot.Repository.database import Base


class Credit(Base):
    __tablename__ = 'credits'
    credit_id = Column(Integer, primary_key=True)
    start_price = Column(Integer)
    start_time = Column(DateTime)
    allowed_duration = Column(Integer, default=1)  # time in hours

    def __init__(self, start_price: int):
        self.start_price = start_price
