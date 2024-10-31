from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Country(Base):
    __tablename__ = 'countries'
    country_id = Column(Integer, primary_key=True)
    name = Column(String)

    # cities = relationship(
    #     "cities",
    #     backref="country",
    # )