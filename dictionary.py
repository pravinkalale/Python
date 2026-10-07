# d = { }             #empty dictionary
# print(type(d))

# s = set()           #empty set  
# print(type(s))       

# my_dict = {1:10, 2:55.5, 3:'x', 4:True, 5:[1,2,3], 6:"hi", 7:10}    #way 1

# my_dict = ({1:10, 2:55.5, 3:'x', 4:True, 5:[1,2,3], 6:"hi", 7:10})    #way 2 

# print(my_dict[5])
# print(my_dict.keys())
# print(my_dict.values())


mydict = {
    "id": 101,
    "name": "pravin",
    "Age": 23
    
}

# i = mydict.items()
# print(i)

mydict.setdefault("city","Pune")
print(mydict)

mydict["city"]="mumbai"
print(mydict)