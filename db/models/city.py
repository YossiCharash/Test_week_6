from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class City(Base):
    __tablename__ = 'cities'
    city_id = Column(Integer, primary_key=True)
    city_name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    country_id = Column(Integer, ForeignKey('country.id'))

    targets = relationship(
        'targets',
        back_populates='cities'
    )

    country = relationship(
        'countrys',
        back_populates='cities'
    )





