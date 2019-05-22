from base import Base
from sqlalchemy import Column, Date, Integer,ForeignKey,String,Boolean,Table
from sqlalchemy.orm import relationship


association_table=Table(
    'association',Base.metadata,
    Column('ticket_no',Integer,ForeignKey('ticket.ticket_no')),
    Column('flight_id',Integer,ForeignKey('flight.flight_id'))
    )


class Flight(Base):
    __tablename__='flight'
    flight_id=Column(Integer,primary_key=True)
    status=Column(Boolean)
    deporture=Column(String)
    arrival=Column(String)
    aircraft_code=Column(Integer,ForeignKey('aircraft.aircraft_code'))
    # Many to One
    aircraft=relationship("Aircraft")
    # Many to Many
    tickets=relationship("Ticket",secondary=association_table,back_populates="flights")

    def __init__(self, flight_id,status,deporture,arrival,aircraft):
        self.flight_id=flight_id
        self.status=status
        self.deporture=deporture
        self.arrival=arrival
        self.aircraft=aircraft
