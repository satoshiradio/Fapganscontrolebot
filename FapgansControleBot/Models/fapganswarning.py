from sqlalchemy import Column, Integer, DateTime, String

from FapgansControleBot.Repository.database import Base


class FapgansWarning(Base):
    __tablename__ = 'warning'
    gans_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    reason = Column(String)
