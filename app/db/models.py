from sqlalchemy import Column, Integer, String, BigInteger, Numeric
from app.db.base import Base

class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True)
    ticker = Column(String, index=True, nullable=False)
    price = Column(Numeric, nullable=False)
    timestamp = Column(BigInteger, index=True, nullable=False)
