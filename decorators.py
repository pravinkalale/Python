# def decor(func):
#     def inner(name):
#         if name == "Priya":
#             print("Hello Priya bad Morning")
#         else:
#             func(name)
#     return inner

# @decor
# def wish(name):
#     print("hello",name,"Good Morning")
# wish("subh")
# wish("Pravin")
# wish("Priya")


#2) we should not use @decor

def decor(func):
    def inner(name):
        if name == "sunny":
            print("Hello sunny Bad morning")
        else:
            func(name)
    return inner 

def wish (name):
    print("Hello",name,"good morning")
    
decorfunction=decor(wish)

wish("durga") #decorator wont be executed
wish("sunny") #decorator wont be executed

decorfunction("durga") #decorator will be executed
decorfunction("sunny") #decorator will be executed