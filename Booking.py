from base import Base
from sqlalchemy import Column, Date, Integer
from sqlalchemy.orm import relationship


class Booking(Base):
    __tablename__ = 'booking'

    book_ref = Column(Integer, primary_key=True)
    total_amount=Column(Integer)
    book_date = Column(Date)
    # One to Many
    tickets=relationship("Ticket")

    def __init__(self,book_ref,total_amoutn,book_date):
        self.book_ref=book_ref
        self.total_amount=total_amoutn
        self.book_date=book_date