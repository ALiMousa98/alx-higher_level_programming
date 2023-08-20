#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password,
        db=database)
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
            ORDER BY states.id ASC"
    cursor.execute(query)

    results = cursor.fetchall()

    cursor.close()
    db.close()

    for row in results:
        print(row)
