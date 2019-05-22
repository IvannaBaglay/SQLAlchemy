

from sqlalchemy import  DDL, event, Table
from base import *


def func ():
    function_1 = DDL("""  
        CREATE OR REPLACE FUNCTION delfunc(id_t integer) RETURNS integer AS $$
       
        BEGIN
         SELECT count (*) into id_t from booking;
         return id_t;
        END;
    $$ LANGUAGE plpgsql;

            """)
    event.listen(Base.metadata, "after_create", function_1)
    connection = engine.raw_connection()
    try:
        cursor = connection.cursor()
        cursor.callproc("delfunc",[1])
        results = list(cursor.fetchall())
        cursor.close()
        connection.commit()
        print(results)
    finally:
        connection.close()
