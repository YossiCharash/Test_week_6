from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Target(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, primary_key=True)
    target_industry = Column(String,nullable=False)
    target_priority = Column(Integer,nullable=True)

    mission_id = Column(Integer, ForeignKey('missions.id'))
    city_id = Column(Integer, ForeignKey('cities.id'))
    target_type_id = Column(Integer, ForeignKey('targettypes.id'))


    missions = relationship(
        "missions",
        back_populates="target",
    )

    city = relationship(
        "cities",
        back_populates="targets",
    )



