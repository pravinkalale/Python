##using function chek the given number is palindrome or not

# num=int(input("Enter a number: "))
# def palindrome(num):
#     temp = num
#     reverse = 0

#     while num>0:
#         rem=num%10
#         reverse=reverse*10+rem
#         num=num // 10
#     if temp==reverse:
#         print("Palindrome")
#     else:
#         print("Not Palindrome")
# palindrome(num)


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

# # Addition using Function

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# def add(a, b):
#     return a + b
# print("Addition =", add(a, b))

# # Multiplication using Function

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# def multiply(a, b):
#     return a * b
# print("Multiplication =", multiply(a, b))

# # Factorial using Function

# n = int(input("Enter a number: "))
# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
#     return fact
# print("Factorial =", factorial(n))

# Armstrong Number using Function

num = int(input("Enter Number: "))

def armstrong(num):

    sum = 0
    temp = num

    while num > 0:
        rem = num % 10
        sum = sum + rem**3
        num = num // 10

    if temp == sum:
        print("Given number is Armstrong number!")
    else:
        print("Given number is not Armstrong number!")

armstrong(num)