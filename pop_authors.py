#!/usr/bin/env python
import psycopg2

DBNAME = "vagrant"


def get_authors():
    """Return the most popular article authors of all time."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from getauthors")
    authors = c.fetchall()
    db.close()
    return authors

for name, views in get_authors():
    print(name + " - " + str(views) + " views")

