#!/usr/bin/env python
import psycopg2

DBNAME = "vagrant"


def get_errors():
    """Return which days more than 1% of requests lead to errors"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from geterrordays")
    errors = c.fetchall()
    db.close()
    return errors

for date, percenterr in get_errors():
    print(date + " - " + str(percenterr) + "% errors")
