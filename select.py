
from base import Session
from Booking import Booking
from Tickets import Ticket
from Flights import Flight
from Aircrafts import Aircraft

def select():
    session = Session()

    select = session.query(Booking) \
        .join(Ticket, Booking.tickets) \
        .join(Flight, Ticket.flights) \
        .filter(Ticket.passenger_name == 'Konrad', Flight.status == True) \
        .all()

    for movie in select:
        print(f'book_ref {movie.book_ref}')
    print('')

    session.commit()
    session.close()