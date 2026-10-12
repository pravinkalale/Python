# def add(a,b):
#      return a+b
# print(add(10,30))


# Factorial using Function

n = int(input("Enter a number: "))
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print("Factorial =", factorial(n)) 