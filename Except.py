# # 1) Basic try - except

# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Error handled")
# print("Program continues")

# # 2) ValueError

# try:
#     x = int("hello")
#     print(x)
# except ValueError:
#     print("invalid value")

# 3) Multiple except blocks

try:
    a = int("10")
    b = 0 
    print(a/b)
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Division Error")