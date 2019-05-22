
from sqlalchemy import  DDL, event, Table
from base import *
def trigger ():
    function = DDL("""                                                                                                                                                       
    CREATE OR REPLACE FUNCTION update_timestamp()
    RETURNS TRIGGER AS $$
    BEGIN
       INSERT INTO AUDIT(EMP_ID, ENTRY_DATE) VALUES (new.book_ref, current_timestamp);
      RETURN NEW;
    END;
    $$ language plpgsql;
    """)



    trigger = DDL("""
    CREATE TRIGGER tr_insert AFTER INSERT
    ON booking FOR EACH ROW EXECUTE PROCEDURE update_timestamp();
    """)
    event.listen(Base.metadata, "after_create", trigger)
    event.listen(Base.metadata, "after_create", function)

    Base.metadata.create_all(engine)

