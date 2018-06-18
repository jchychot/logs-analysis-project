#!/usr/bin/env python
import psycopg2

DBNAME = "vagrant"


def get_articals():
    """Return the most popular three articles of all time."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from gettopthree;")
    articals = c.fetchall()
    db.close()
    return articals


for title, views in get_articals():
    print('"' + title + '" - ' + str(views) + " views")
