import sqlite3 as sq

con = sq.connect("mydata.db")

cur = con.cursor()

# cur.execute("create table student(id int, name text)")
cur.execute("insert into student(id, name) values(?,?)", (1,'Pravin'))

con.commit()

con.close()
