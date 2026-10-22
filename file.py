# f = open("pravin.txt","w")
# f.write("hello my name is pravin\n")
# f.close()

# f = open("pravin.txt","r")
# print(f.read())
# f.close()

# f = open("pravin.txt","a")
# f.write("i am from nanded\n")
# f.close()

# with statement

with open("pravin.txt","r") as f:
    data = f.read()
    print(data)
    
# with open("pravin.txt","a") as f:
#     f.write("\n i'm learning python programming")
    