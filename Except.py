# 1) Basic try - except

try:
    print(10/0)
except ZeroDivisionError:
    print("Error handled")
print("Program continues")

# 2) ValueError

try:
    x = int("hello")
    print(x)
except ValueError:
    print("invalid value")

# 3) Multiple except blocks

try:
    a = int("10")
    b = 0 
    print(a/b)
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Division Error")

# 4) else block

try:
    x = 10 + 5
except ValueError:
    print("Error")
else:
    print("Result:",x)

# 5) finally block

try:
    print("A")
    print(10/0)
except ZeroDivisionError:
    print("B")
finally:
    print("C")

# 6) return and finally

def test():
    try:
        return 10
    finally:
        print("Finally executed")
print(test())

# 7) code after exception 

try:
    print("One")
    x = 10/0
    print("Two")
except ZeroDivisionError:
    print("Three")
print("Four")

# 8) raise keyword

age = 16
try:
    if age < 18:
        raise ValueError("underage")
    print("Eligible")
except ValueError as e:
    print(e)

# 9) Custome Exception 

class TooYoungException(Exception):
    pass
 
age  = 17

try:
    if age < 18:
        raise TooYoungException("Age must be 18+")
except TooYoungException as e:
    print("Caught:",e)
    
# 10) nested exception handling 

try:
    print("Outer start")
    try:
        print(5/0)
    except ZeroDivisionError:
        print("Inner handled")
    print("Outer end")
except Exception:
    print("Outer handled")