#!/usr/bin/python3
"""takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument"""


import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    statename=sys.argv[4]

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
    WHERE states.name LIKE '{}' ORDER BY id ASC".format(statename))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
        
