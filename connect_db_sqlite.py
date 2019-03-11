#!/usr/bin/env python3

import sqlite3

def main():
    print("1. Connect to test database.")    
    db = sqlite3.connect('test.db')
    cur = db.cursor()

    print("2. Create table")
    cur.execute("DROP TABLE IF EXISTS employee")
    cur.execute("""
        CREATE TABLE employee (
            ID INT PRIMARY KEY     NOT NULL,
            NAME           TEXT    NOT NULL,
            AGE            INT     NOT NULL,
            ADDRESS        CHAR(50),
            SALARY         REAL
        )
        """)

    print("3. Insert row")
    cur.execute("INSERT INTO employee (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )")

    print("4. Insert row")
    cur.execute("INSERT INTO employee (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

    print("5. Insert row")
    cur.execute("INSERT INTO employee (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

    print("6. Insert row")
    cur.execute("INSERT INTO employee (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

    print("7. Commit")
    db.commit()

    print("8. Get count")
    cur.execute("SELECT COUNT(*) FROM employee")
    count = cur.fetchone()[0]
    print(f'There are {count} rows in the table')

    print("9. Read full table")
    for curr_row in cur.execute("SELECT * FROM employee"):
        print(curr_row)

    print("10. Close connection")    
    db.close()

if __name__ == "__main__":
    main()