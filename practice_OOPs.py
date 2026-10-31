# class Student:
#     def __init__(self):
#         self.name = "Pravin"
#         self.age = 23
#     def show(self):
#         print("my name is:",self.name)  
#         print("I'm",self.age,"years old")  
# s1 = Student()
# s1.show()

# class Sample:
#     def show(self):
#         print("hello world")

# s1 = Sample()
# s1.show()

"""single inheritance"""

# class parent:
#     def speak(self):
#         print("parents talking")
        
# class child(parent):
#     def ch(self):
#         print("listing childrens")
        
# O = child()
# O.ch()
# O.speak()

"""Multilevel inheritance"""

class parent:
    def speak(self):
        print("parents speaking")
 
class child(parent):
    def aqua(self):
        print("child aquires parent behaviour")
        
p = child()
p.speak()
p.aqua()