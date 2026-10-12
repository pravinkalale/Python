# #default function / non parameterized

# def display():       #func definition
#     print("Hello")   #func body
# display()            #fun calling
# print("welcome to python jungle")
# display()            #fun calling


# #parameterized function 

# def add(a,b):  #a and b is parameter
#     print(a+b)
# add(10,20)     # 10 and 20 is Arguments


# num = 234
# reverse = 0
# temp = num 
# def pk(a):
#     while num > 0:
#         rem = num % 10
#         reverse = reverse * 10 + rem
#         num = num // 10
#     # print(a)
# if temp == reverse:
#     print("palindrome number")
# else: 
#     print("not palindrome")
  
  
    
# num = 234
# temp = num

# def pk(a):
#     reverse = 0

#     while a > 0:
#         rem = a % 10
#         reverse = reverse * 10 + rem
#         a = a // 10

#     return reverse

# reverse = pk(num)

# if temp == reverse:
#     print("palindrome number")
# else:
#     print("not palindrome")
    
#put two aruments and paramenter

# def show(name,city="Pune"):
#     print("hello my name is",name,"and i am from",city)
# show("Aryan")
# show("Ajinkya","Mumbai")

# def show(name,age,city):
#     print("my name is:",name,
#           "I'm",age,"years old",
#           "I'm leaving in:",city)
# show(name="pravin", age=23, city="Pune")

# def show(name,*value):      #variable length argument using(*)
#     print(name,value)
# show("Arya",10,20,30)
# show("vihan",10,20,30,40,50)

def show(*value):
    total = 0
    
    for i in value:
        total = total + i
        
    print("Total:",total)
    
show(10,20,30,40)  #100
show(10,20)        #30
show(10,20,30)     #60