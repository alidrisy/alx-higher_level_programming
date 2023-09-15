#!/usr/bin/python3
"""This script lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa"""
from sys import argv
import MySQLdb


if __name__ == '__main__':
    con = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])
    curs = con.cursor()
    curs.execute("SELECT states.id, states.name FROM states WHERE states.name LIKE 'N%'\
            ORDER BY states.id ASC;")
    rows = curs.fetchall()

    for row in rows:
        print(row)

    curs.close()
    con.close()
