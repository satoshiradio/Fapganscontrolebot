from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from FapgansControleBot.Repository.database import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_telegram_id = Column(Integer, nullable=False)
    user_username = Column(String(256))
    ganzen = relationship("Gans", back_populates="user", cascade="all, delete, delete-orphan")

    def __init__(self, user_telegram_id: int, username: str):
        self.user_telegram_id = user_telegram_id
        self.user_username = username

    def set_username(self, username: str):
        self.user_username = username
