# num = int(input("Enter a Number: "))

# for i in range(1,11):
#     print(num * i)
    
# factorial numbers

num = int(input("Enter a number: "))
def factorial(num):
    
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact     
print("factorial: " ,factorial(num))