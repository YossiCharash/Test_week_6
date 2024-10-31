from sqlalchemy import Column, Date, Table, Float, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from sqlalchemy.orm import declarative_base


# from db.models.missions import target_mission_relation

Base = declarative_base()

target_mission_relation = Table(
    'target_mission_relation',
    Base.metadata,
    Column('target_id', Integer, ForeignKey('targets.target_id')),
    Column('mission_id', Integer, ForeignKey('missions.mission_id'))
)


class Target(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, primary_key=True)
    target_industry = Column(String,nullable=False)
    target_priority = Column(Integer,nullable=True)

    mission_id = Column(Integer, ForeignKey('missions.mission_id'))
    city_id = Column(Integer, ForeignKey('cities.city_id'))
    target_type_id = Column(Integer, ForeignKey('targettypes.id'))


    missions = relationship(
        "Missions",
        secondary=target_mission_relation,
        back_populates="targets",
    )

    city = relationship(
        "City",
        back_populates="targets",
    )


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


    # target_id = Column(Integer, ForeignKey('targets.target_id'))

    targets = relationship(
        'Target',
        secondary=target_mission_relation,
        back_populates="missions",
    )



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
        'countries',
        back_populates='cities'
    )










