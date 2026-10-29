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


# import sqlite3 as sq

# con = sq.connect("mydata.db")
# cur = con.cursor()

# cur.execute("""
#     DELETE FROM student
#     WHERE rowid = (
#         SELECT rowid
#         FROM student
#         WHERE id = ? AND name = ?
#         LIMIT 1
#     )
# """, (1, "Pravin"))

# con.commit()

# cur.execute("SELECT * FROM student")
# print(cur.fetchall())

# con.close()

########################################################

# import sqlite3 as sq

# con = sq.connect("mydata.db")

# cur = con.cursor()
# # cur.execute("CREATE TABLE Pk(id int, name text, city text)")
# # cur.execute("INSERT INTO Pk(id, name, city) Values(?, ?, ?)", (1, 'Priya', 'Nanded'))

# con.commit()
# cur.execute("delete from Pk id = 1")
# # cur.execute("SELECT * FROM Pk")
# # data = cur.fetchall()
# # print(data)
# con.close()

## delete data from table

# import sqlite3 as sq 

# con = sq.connect("mydata.db")

# cur = con.cursor()
# cur.execute("DELETE FROM Pk where id = 1")

# con.commit()
# con.close()

## Insert data in existing table

# import sqlite3 as sq 

# con = sq.connect("mydata.db")
# cur = con.cursor()

# cur.execute("INSERT INTO Pk(id, name, city) Values(?, ?, ?)", (1,'priya','nashik'))

# con.commit()
# con.close()

## store many data at a time 

# import sqlite3 as sq 

# con = sq.connect("mydata.db")
# cur = con.cursor()

# p = [(2,'Pravin','Nanded'),(3,'Gajanan','Nanded')]

# cur.executemany("INSERT INTO Pk Values(?,?,?)",p)

# con.commit()
# con.close()

## fetch One Data 

# import sqlite3 as sq 

# con = sq.connect("mydata.db")

# cur = con.cursor()
# cur.execute("SELECT * FROM Pk WHERE id = ?",[2])
# data = cur.fetchone()

# con.commit()
# print(data)
# con.close()

# import sqlite3 as sq 

# con = sq.connect("mydata.db")

# cur = con.cursor()

# cur.execute("SELECT * FROM student")
# data = cur.fetchall 
# print(data)

# con.commit()
# con.close()

""" insert multiple values"""


import sqlite3 as sq 

con = sq.connect("mydata.db")

cur = con.cursor()

# p = [(2,'Priya'),(3,'Shiv'),(4,'arjun')]

# cur.executemany("INSERT INTO student Values (?,?)",p)
# data = cur.execute("SELECT * FROM student")

# for row in data:
#     print(row[0],row[1])
# print(data)

# cur.execute("SELECT * FROM student")
# data = cur.fetchall()
# print("total rows=",len(data))

# for row in data:
#     print(row[0],row[1])

# cur.execute("SELECT * FROM student WHERE id = ?",[2])
# data = cur.fetchone()
# print(data)

# cur.execute("UPDATE student set name = 'gaurav' where id = 2")

# cur.execute("delete from student where id = 3")

con.commit()
con.close()


""" retrive data from database"""

# data = cur.execute("SELECT * FROM student")

# for row in data:
#     print(row[0],row[1])
# print(data)

"""fetch all data"""

# cur.execute("SELECT * FROM student")
# data = cur.fetchall()
# print("total rows=",len(data))

# for row in data:
#     print(row[0],row[1])

# print(data)

"""fetch one particular data from table"""

# cur.execute("SELECT * FROM student WHERE id = ?",[2])
# data = cur.fetchone()
# print(data)

"""update command"""

# cur.execute("SELECT * FROM student WHERE id = ?",[2])
# data = cur.fetchone()
# print(data)

"""Delete particular data"""

# cur.execute("delete from student where id = 3")