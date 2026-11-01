# # Single inheritance with constructors

# class Animal:
#     def __init__(self, name):
#         self.name = name
        
#     def speak(self):
#         print(self.name ,"is speaking")

# class Dog(Animal):
#     def bark(self):
#         print("dog is barking")
        
# d = Dog("Animal")
# d.bark()
# d.speak()

"""Multilevel inheritance with constructores"""

# class Grand_parent:
#     def __init__ (self):
#         print("Grand parent constructor")
        
        
#     def talk(self):
#         print("grand parents talk")
        
# class Parent(Grand_parent):
#     def __init__(self):
#         print("Parent constructor")
        
        
#     def ride(self):
#         print("bike riding")

# class Child(Parent):
#     def __init__(self):
#         print("child constructor")
           
#     def drive(self):
#         print("car driving")

# d = Child()
# d.talk()
# d.ride()
# d.drive()

"""Multiple inheritance with constructors"""

# class Calculation1:

#     def __init__(self):
#         print("Calculation1 Constructor")

#     def summation(self, a, b):
#         return a + b


# class Calculation2:

#     def __init__(self):
#         print("Calculation2 Constructor")

#     def difference(self, a, b):
#         return a - b


# class Derived(Calculation1, Calculation2):

#     def __init__(self):
#         print("Derived Constructor")

#     def divide(self, a, b):
#         return a / b


# d = Derived()

# print(d.summation(10, 20))
# print(d.difference(10, 20))
# print(d.divide(10, 20))

"""Hierarchical inheritance with constructor"""

class Animal:
    def __init__(self):
        print("Animal constructor")
        
    def eat(self):
        print("Animal eating")

class Dog(Animal):
    def __init__(self):
        print("Dog constructor")
        
    def bark(self):
        print("Dog bark")
        
class Cat(Animal):
    def __init__(self):
        print("Cat constructor")
        
    def meow(self):
        print("cat meow")
        
d = Dog()
d.eat()
d.bark()

c = Cat()
c.eat()
c.meow()
