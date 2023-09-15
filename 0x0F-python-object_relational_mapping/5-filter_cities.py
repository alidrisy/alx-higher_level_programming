#!/usr/bin/python3
"""This script takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa"""
from sys import argv
import MySQLdb


if __name__ == '__main__':
    con = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])
    curs = con.cursor()
    curs.execute("SELECT cities.name, cities.id FROM states, cities WHERE\
            states.id = cities.state_id AND states.name = %s ORDER BY\
            cities.id ASC;", (argv[4], ))
    rows = curs.fetchall()

    x = len(rows)
    for r in range(x):
        print(rows[r][0], end='')
        if r != x - 1:
            print(', ', end='')
    print()

    curs.close()
    con.close()
