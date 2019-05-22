from base import Base
from sqlalchemy import Column, Date, Integer,ForeignKey,String
from sqlalchemy.orm import relationship

class Aircraft(Base):
    __tablename__='aircraft'

    aircraft_code = Column(Integer,primary_key=True)
    model=Column(Integer)
    def __init__(self,aircraft_code,model):
        self.aircraft_code=aircraft_code
        self.model=model




