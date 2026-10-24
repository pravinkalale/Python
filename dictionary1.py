# d = {1:'Abc', 2:'Lmn', 3:'Pqr', 4:'Xyz'}
# print(d)

# #Accesing value using keys
# print("first name is: "+ d[1])
# print("second name is: "+ d[2])

# print(d.keys())
# print(d.values())

#Dictionary special methods

#get()

# Mydict = {
#     "Id": 101,
#     "Name": "Merry",
#     "Age": 19
# }

# # print(Mydict["Name"])
# p = Mydict.get("Name")
# print(p)

#copy() method

# Mydict = {
#     "Id": 101,
#     "Name": "Merry",
#     "Age": 19
# }
# c = Mydict.copy()
# print(c)

# #pop() method

# Mydict = {
#     "Id": 101,
#     "Name": "Merry",
#     "Age": 19
# }
# Mydict.pop("Age")
# print(Mydict)

# #sorted() method 

# names = {1:'Pune', 2:'Satara', 3:'Sangali', 4:'Nanded'}
# print(sorted(names.keys()))
# print(sorted(names.items()))
# print(sorted(names.values()))

#items() method 

# mydict = {
#     "id": 101,
#     "Name": "Merry",
#     "Age": 19
# }
# i = mydict.items()
# print(i)

#popitem() method 

# mydict = {
#     "id": 101,
#     "Name": "Merry",
#     "Age": 19
# }
# p = mydict.popitem()
# print(p)

# #update() method

# mydict = {
#     "id": 101,
#     "Name":"Merry",
#     "Age": 19
# }
# mydict.update({"city":"Pune"})
# print(mydict)

#setdefault() method 

mydict = {
    "id": 101,
    "Name":"Merry",
    "Age": 19
}    
mydict.setdefault("City","Pune")
print(mydict)