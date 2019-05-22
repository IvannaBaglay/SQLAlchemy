# 1 - imports

from base import Session
from Booking import Booking
from Tickets import Ticket
from Flights import Flight
from Aircrafts import Aircraft

def queries():
    # 2 - extract a session
    session = Session()

    # 3 - extract all movies
    booking = session.query(Booking).all()

    # 4 - print movies' details
    print('\n### All movies:')
    for i in booking:
        print(f'{i.book_ref} was released on {i.book_date}')
    print('')

    session.close()