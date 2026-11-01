# (multilevel inheritance) multiple classes and objects

class Grand_parent:                      # grand class 
    def talk(self):
        print("grand parents talk")
        
class parent(Grand_parent):
    def ride(self):
        print("bike riding")
        
class child(parent):
    def drive(self):
        print("car driving")
d = child()
d.ride()
d.talk()
d.drive()

# class Parent:
#     def __init__(self):
#         print("Parent constructor")
    
# class Child(Parent):
#     def __init__(self):
#         print("Child constructor")
        
# obj = Child()
