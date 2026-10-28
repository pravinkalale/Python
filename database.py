# import sqlite3 as sq

# con = sq.connect("mydata.db")

# cur = con.cursor()

# # cur.execute("create table student(id int, name text)")
# cur.execute("insert into student(id, name) values(?,?)", (1,'Pravin'))

# con.commit()

# #Fetch data
# cur.execute("SELECT * FROM student")
# data = cur.fetchall()
# print(data)

# con.close()


import sqlite3 as sq

con = sq.connect("mydata.db")
cur = con.cursor()

cur.execute("""
    DELETE FROM student
    WHERE rowid = (
        SELECT rowid
        FROM student
        WHERE id = ? AND name = ?
        LIMIT 1
    )
""", (1, "Pravin"))

con.commit()

cur.execute("SELECT * FROM student")
print(cur.fetchall())

con.close()