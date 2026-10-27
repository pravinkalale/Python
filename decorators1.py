# 1) Basic decorator


def my_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@my_decorator
def greet():
    print("Hello")

greet()


# 2) without return func()


def decor(func):
    def wrapper():
        print("A")
        func()
        print("B")
    return wrapper

@decor
def show():
    print("Python")

show()


# 3) Multiple decorator calls


def decor(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decor
@decor
def hello():
    print("Hello")

hello()


# 4) with Arguments


def decor(func):
    def wrapper(name):
        print("Welcome message:")
        func(name)
    return wrapper

@decor
def greet(name):
    print("Hello", name)

greet("Pravin")


# 5) Decorator Execution Order


def decor(func):
    print("Decorator called")

    def wrapper():
        print("Wrapper called")
        func()

    return wrapper
 
@decor
def test():
    print("Test called")

print("Main program")
test()
