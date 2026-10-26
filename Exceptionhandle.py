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
 
# try:
#     x = int(input("Enter first number: "))
#     y = int(input("Enter second number: "))
#     print(x/y)
# except ArithmeticError:
#     print("Arithmetic error occurred.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
    
    
class TooYoungException(Exception):
    def _init_(self,arg):
        self.msg=arg
        
        
class TooOldException(Exception):
    def _init_(self,arg):
        self.msg=arg
        
        
age = int(input("Enter Age: "))
if age > 60:
    raise TooOldException("Your age already crossed marriage age ... no chance of getting marriage")
elif age < 18:
    raise TooYoungException("Plz wait some more time you will get best match soon")
else:
    print("sorry")
        
    
##############################

# class TooYoungException(Exception):
#     def __init__(self, arg):
#         self.msg = arg


# class TooOldException(Exception):
#     def __init__(self, arg):
#         self.msg = arg


# try:
#     age = int(input("Enter Age: "))

#     if age > 60:
#         raise TooOldException(
#             "Your age has crossed the marriage age... no chance of getting married"
#         )

#     elif age < 18:
#         raise TooYoungException(
#             "Please wait some more time. You will get the best match soon."
#         )

#     else:
#         print("You are eligible for marriage.")

# except TooYoungException as e:
#     print(e.msg)

# except TooOldException as e:
#     print(e.msg)

# except ValueError:
#     print("Please enter a valid number.")