# # 1) Basic try - except

# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Error handled")
# print("Program continues")

# 2) ValueError

try:
    x = int("hello")
    print(x)
except ValueError:
    print("invalid value")