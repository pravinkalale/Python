# a = 10
# b = 0

# try:
#     print(a / b)

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# print("Program completed")


#abnormal termination of program
# print ("stmt-1")
# print(10/0)
# print("stmt -3")

#normal termination of program 

# print ("stmt-1")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print(10/2)
# print("stmt -3")


# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a number: "))
#     print(a/b)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
 
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(x/y)
except ArithmeticError:
    print("Arithmetic error occurred.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
    
    