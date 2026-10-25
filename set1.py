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


#Set Methods 

s = {10,20,30,20,10}
s.add(50)
s.update([60,70])
s.remove(50)
s.discard(100)
s.pop()
s.clear()
print(s)
