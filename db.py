"""Create database and table"""

# import sqlite3 as sq 

# con = sq.connect("pmk.db")

# cur = con.cursor()

# cur.execute("CREATE TABLE IF NOT EXISTS employees(id int, Name text, salary int, city text, cont text)")

# con.commit()

# con.close()

"""Insert data into table"""

# import sqlite3 as sq 

# con = sq.connect("pmk.db")

# cur = con.cursor()

# cur.execute("INSERT INTO employees(id, Name, salary, city, cont)Values(?,?,?,?,?)",(1, 'Amit', 30000, 'Nanded', '9011265475'))

# con.commit()

# con.close()

"""Insert multiple data at a time in table"""

# import sqlite3 as sq 
# con = sq.connect("pmk.db")
# cur = con.cursor()

# l = [(2,'Pradip',25000,'Nanded','7588963320'),
#      (3,'Vaibhav',20000,'Nanded','8080903993'),
#      (4,'Balaji',30000,'Pune','4578965230'),
#      (5,'Krishna',35000,'Nashik','9875632210')]

# cur.executemany("INSERT INTO employees Values(?,?,?,?,?)",l)

# con.commit()
# con.close()


"""Fetch all data"""

import sqlite3 as sq 
con = sq.connect("pmk.db")
cur = con.cursor()

cur.execute("SELECT * FROM employees")
data = cur.fetchall()

for row in data:
    print(row)
    
con.commit()
con.close()