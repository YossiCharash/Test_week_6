from sqlalchemy import Column, Integer, Date, Float

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Missions(Base):
    __tablename__ = 'missions'
    mission_id = Column(Integer, primary_key=True)
    mission_date = Column(Date,nullable=True)
    airborne_aircraft = Column(Float,nullable=True)
    attacking_aircraft =Column(Float,nullable=True)
    bombing_aircraft = Column(Float,nullable=True)
    aircraft_returned = Column(Float,nullable=True)
    aircraft_failed = Column(Float,nullable=True)
    aircraft_damaged = Column(Float,nullable=True)
    aircraft_lost = Column(Float,nullable=True)