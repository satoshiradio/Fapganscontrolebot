from sqlalchemy import Column, Integer, String, DateTime


class Gans:
    __tablename__ = 'gans'
    gans_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    date = Column(DateTime)
