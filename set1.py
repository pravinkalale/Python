# #Removing duplicate values
# numbers = {10,20,30,40,20,10,30}
# print(numbers)

# #create empty set 
# a = set()
# b = {}
# print(type(a))
# print(type(b))

# s = {10,20,30,20,10}
# s.add(40)
# s.discard(20)
# print(len(s))
# print(10 in s)

# #Example
# students = {"Pravin","Amit","Rahul","Pravin","Amit"}
# print(students)
# print("Total unique students:", len(students))


# #Set Methods 

# s = {10,20,30,20,10}
# s.add(50)
# s.update([60,70])
# s.remove(50)
# s.discard(100)
# s.pop()
# s.clear()
# print(s)

#Set Operations

a = {1,2,3,4}
b = {3,4,5,6}

print(a|b)      #Union
print(a & b)    #intersection 
print(a - b)    #difference a-b
print(b - a)    #difference b -a
print(a ^ b)    #symmetric difference
print(b.issubset(a))
print(a.issubset(b))
a.intersection_update(b)
print(a)