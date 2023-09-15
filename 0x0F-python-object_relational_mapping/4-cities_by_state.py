#!/usr/bin/python3
"""This script lists all cities from the database hbtn_0e_4_usa"""
from sys import argv
import MySQLdb


if __name__ == '__main__':
    con = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])
    curs = con.cursor()
    curs.execute("SELECT cities.id, cities.name, states.name FROM states,\
            cities WHERE states.id = cities.state_id;")
    rows = curs.fetchall()

    for row in rows:
        print(row)

    curs.close()
    con.close()
