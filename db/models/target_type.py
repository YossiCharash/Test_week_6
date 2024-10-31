from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class TargetType(Base):
    __tablename__ = 'targettypes'
    target_type_id = Column(Integer, primary_key=True)
    target_type_name = Column(String)


    targets = relationship(
        "targets",
        back_populates="targettypes",
    )