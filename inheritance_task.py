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

class Grand_parent:
    def __init__ (self):
        print("Grand parent constructor")
        
        
    def talk(self):
        print("grand parents talk")
        
class Parent(Grand_parent):
    def __init__(self):
        print("Parent constructor")
        
        
    def ride(self):
        print("bike riding")

class Child(Parent):
    def __init__(self):
        print("child constructor")
        
        
    def drive(self):
        print("car driving")

d = Child()
d.talk()
d.ride()
d.drive()