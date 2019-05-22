from base import Base
from sqlalchemy import Column, Date, Integer,ForeignKey,String
from sqlalchemy.orm import relationship

from Flights import association_table

class Ticket(Base):
    __tablename__='ticket'
    ticket_no = Column(Integer,primary_key=True)
    # One to Many
    book_ref =Column(Integer,ForeignKey('booking.book_ref'))
    passenger_id=Column(Integer)
    passenger_name=Column(String)
    # Many to Many
    flights = relationship("Flight", secondary=association_table, back_populates="tickets")

    def __init__(self,ticket_no,book_ref,passenger_id,passenger_name):
        self.ticket_no=ticket_no
        self.book_ref=book_ref
        self.passenger_id=passenger_id
        self.passenger_name=passenger_name

