students = ["Amit", "Rahul", "Priya"]
 
# for i in students:    #this is iterable
#     print(i)

# iterator = iter(students)    #this is iterator method 

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# def students():            #this id generator function
#     yield "Amit"
#     yield "Rahul"
#     yield "Priya"

# s = students()
# for i in s:
#     print(i)
    

#To generate fibonacci numbers using normal function and generator function 

def fibonacci(n):
    a = 0
    b = 1
    
    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c
fibonacci(10)


# def fibonacci(n):
#     a = 0 
#     b = 1
#     for i in range(n):
#         c = a + b
#         a = b
#         b = c
#     print(a)
# fibonacci(5)