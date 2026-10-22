f = open("demo.txt","w")
f.write("hello my name is pravin\n")
f.close()

# file = open("demo.txt","r")
# print("file_name",file.name)
# print("readable_mode", file.readable())
# print("writable_mode",file.writable())
# print("file_closed",file.closed)
# file.close()

# #Read
# f = open("demo.txt","r")
# print(f.read())
# f.close()

# #write data into file using w mode
# #but existing daya is automatically remove
# f = open("demo.txt","w")
# f.write("hello my name is pedha\n")
# f.close()

# # Apend
# #write data into file using append mode 
# #but existing data is still remaining

# f = open("demo.txt","a")
# # f.write("hello my name is pedha\n")
# f.write("I am from Nanded")
# f.close()

# import os
 
# f = open("demo.txt","r")
# print(f.readline())
# print(f.readline())

# import os
# f = open("demo1.txt","x")
# f.close()

# f = open("demo1.txt","w")
# f.write("hii Priya\n")
# f.close()

# #Delete the file 
# import os
# os.remove("demo1.txt")

# # check if file exists, then delete it 

# import os
# if os.path.exists("demo1.txt"):
#     os.remove("demo1.txt")
# else:
#     print("the file does not exit")

# f = open("demo.txt","a")
# f.write("i have a completed MCA\n")
# f.close()

# f = open("demo.txt","r")
# print(f.readline())
# print(f.readline())


# f = open("demo.txt","r")
# print(f.readlines())

#with statement
with open("demo.txt","r") as f:
    content = f.read();
    print(content)
        