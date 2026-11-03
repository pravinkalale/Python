# varible number of a

# class Test:
#     def sum(self,*a):
#         total = 0
#         for x in a:
#             total = total + x
#         print("The Sum:",total)
        
# t = Test()
# t.sum(10,20)
# t.sum(10,20,30)
# t.sum(10)
# t.sum()


"""method Overriding"""


# class P:
#     def property(self):
#         print("Gold+Land+cash+Power")
#     def marry(self):
#         print("Ranumandal")
# class C(P):
#     def marry(self):
#         print("Katrina kaif")

# c = C()
# c.property()
# c.marry()

"""method Overriding using super() method"""

# class P:
#     def property(self):
#         print("Gold+Land+cash+Power")
#     def marry(self):
#         print("Ranumandal")
# class C(P):
#     def marry(self):
#         super().marry()
#         print("Katrina kaif")

# c = C()
# c.property()
# c.marry()

"""constructor Overriding"""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self,name, age, eno, esal):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal 
    
    def display(self):
        print("Employee Name:",self.name)
        print("Employee Age:", self.age)
        print("Employee Number:", self.eno)
        print("Employee salary:", self.esal)
        
e1 = Employee('pravin',23,854,40000)
e1.display()
e2 = Employee('gaurav',22,254,30000)
e2.display()
