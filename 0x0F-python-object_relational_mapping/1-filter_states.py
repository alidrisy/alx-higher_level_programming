#!/usr/bin/python3
"""This script lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa"""
from sys import argv
import MySQLdb


if __name__ == '__main__':
    con = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3], charset="utf8")
    curs = con.cursor()
    curs.execute("SELECT * FROM states WHERE CONVERT(`name` USING Latin1)\
            COLLATE Latin1_General_CS LIKE 'N%' ORDER BY id")
    rows = curs.fetchall()

    for row in rows:
        print(row)

    curs.close()
    con.close()
