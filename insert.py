from datetime import date
from base import Session, engine, Base
from Booking import Booking
from Tickets import Ticket
from Flights import Flight
from Aircrafts import Aircraft

def insert():
    # 2 - generate database schema


    # 3 - create a new session
    session = Session()

    aircraft1 = Aircraft(313, 789)
    aircraft2 = Aircraft(314, 780)
    aircraft3 = Aircraft(315, 781)
    aircraft4 = Aircraft(316, 782)

    booking1 = Booking(1, 1, date(2018, 10, 12))
    booking2 = Booking(2, 1, date(2018, 10, 13))
    booking3 = Booking(3, 1, date(2018, 10, 14))
    booking4 = Booking(4, 1, date(2018, 10, 15))

    ticket1 = Ticket(1, 1, 12, "Konrad")
    ticket2 = Ticket(2, 2, 12, "Konrad")
    ticket3 = Ticket(3, 3, 12, "Horus")
    ticket4 = Ticket(4, 4, 12, "Perturabo")

    flight1 = Flight(1, True, "A1", "B1", aircraft1)
    flight2 = Flight(2, False, "A2", "B2", aircraft2)
    flight3 = Flight(3, True, "A3", "B3", aircraft3)
    flight4 = Flight(4, True, "A4", "B4", aircraft4)

    ticket1.flights = [flight1]
    flight1.tickets = [ticket1]
    ticket2.flights = [flight2]
    flight2.tickets = [ticket2]
    ticket3.flights = [flight3]
    flight3.tickets = [ticket3]
    ticket4.flights = [flight4]
    flight4.tickets = [ticket4]

    session.add(aircraft1)
    session.add(booking1)
    session.add(ticket1)
    session.add(flight1)

    session.add(aircraft2)
    session.add(booking2)
    session.add(ticket2)
    session.add(flight2)

    session.add(aircraft3)
    session.add(booking3)
    session.add(ticket3)
    session.add(flight3)

    session.add(aircraft4)
    session.add(booking4)
    session.add(ticket4)
    session.add(flight4)

    session.commit()

    session.close()


def delete():
     Base.metadata.drop_all(engine)

