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

# # Multiplication using Function

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# def multiply(a, b):
#     return a * b
# print("Multiplication =", multiply(a, b))

# # Addition using Function

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# def add(a, b):
#     return a + b
# print("Addition =", add(a, b))

# # Reverse a Number using Function

# n = int(input("Enter a number: "))
# def reverse(num):
#     rev = 0
#     while num > 0:
#         rem = num % 10
#         rev = rev * 10 + rem
#         num = num // 10
#     return rev
# print("Reverse =", reverse(n))

# sum of digits 


def digit_sum(num):
    total = 0

    while num > 0:
        rem = num % 10
        total = total + rem
        num = num // 10

    return total


print(digit_sum(1234))
