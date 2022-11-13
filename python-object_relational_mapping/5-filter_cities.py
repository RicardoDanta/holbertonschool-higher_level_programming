#!/usr/bin/python3
"""Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()

    x = "SELECT cities.name\
        FROM cities\
        JOIN states ON cities.state_id = states.id\
        WHERE states.name = %(state)s\
        ORDER BY cities.id"
    cur.execute(x, {"state": sys.argv[4]})
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
