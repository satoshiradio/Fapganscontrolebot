from sqlalchemy import Column, Integer, DateTime, String


class Warning:
    __tablename__ = 'warning'
    gans_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    date = Column(DateTime)
    reason = Column(String)