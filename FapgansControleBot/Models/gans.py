import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from FapgansControleBot.Repository.database import Base


class Gans(Base):
    __tablename__ = 'gans'
    gans_id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.user_id'))
    credit_id = Column(ForeignKey('credits.credit_id'))
    date = Column(DateTime)
    user = relationship("User", back_populates="ganzen")

    def __init__(self, user_id: int):
        self.user_id = user_id
        self.date = datetime.datetime.utcnow()
