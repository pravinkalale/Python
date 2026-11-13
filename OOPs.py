# class Student:
#     def __init__(self, name, age, marks):
#         self.name = name      
#         self.age = age            #instance variables
#         self.marks = marks
        
#     def talk(self):      # instance method
        
#         print("Hello my Name is :",self.name)
#         print("my age is :",self.age)
#         print("my marks are :",self.marks)
        
# s = Student("bhranti",18,80)
# s.talk()


# class Parent:
#     def old(self):
#         print("i am parent")
        
# class Child(Parent):
#     def young(self):
#         print("i am young")

# d = Child()
# d.young()

"""10/11/2026"""

# class Student:
#     def __init__(self, fullname, marks):
#         self.name = fullname
#         self.marks = marks
#         print("adding new student in database..")
        
# s1 = Student("Pravin", 98)
# print(s1.name, s1.marks)

# s2 = Student("shradha didi",76)
# print(s2.name, s2.marks)

# """Create Account class with 2 attributes - balance & account no.
# create methods for debit, credit & printing the balance."""

# class Account:
#     def __init__(self,bal, acc):
#         self.balance = bal
#         self.account_no = acc
     
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("total balance =", self.get_balance())
        
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited")
#         print("total balance =", self.get_balance())
        
#     def get_balance(self):
#         return self.balance
         
# acc1 = Account(10000, 14125466)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(40000)
# acc1.debit(10000)


"""Single inheritance"""

# class Animal:
#     def speak(self):
#         print("Animal Speaking")
# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")
        
# d = Dog()
# d.speak()
# d.bark()

"""using constructor"""

# class Animal:
#     def __init__(self, name):
#         self.name = name
        
#     def speak(self):
#         print(self.name, "is speaking")
        
# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# d = Dog("Animal")
# d.speak()
# d.bark()

"""Multilevel inheritance"""

# class Grand_parent:
#     def house(self):
#         print("Grand parent's house")
        
# class parent(Grand_parent):
#     def car(self):
#         print("Parent's car")
    
# class child(parent):
#     def bike(self):
#         print("child's bike")
        
# c = child()
# c.house()
# c.car()
# c.bike()

"""using constructor"""

# class Grand_parent:
#     def __init__(self):
#         print("Grand parent constructor")
    
#     def house(self):
#         print("Grand parent's house")
        
# class parent(Grand_parent):
#     def car(self):
#         print("Parent's car")
    
# class child(parent):
#     def bike(self):
#         print("child's bike")
        
# c = child()
# c.house()
# c.car()
# c.bike()


"""multiple inheritance"""

# class Calculation1:
#     def summation(self, a,b):
#         return a+b
    
# class Calculation2:
#     def multiplication(self, a,b):
#         return a*b

# class Derived(Calculation1, Calculation2):
#     def divid(self, a,b):
#         return a/b
    
# d = Derived()
# print(d.summation(10,30))
# print(d.multiplication(10,30))
# print(d.divid(10,30))


"""Hierarchical Inheritance"""

class Animal:
    def eat(self):
        print("Animal can eat")
        
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
        
class Cat(Animal):
    def meow(self):
        print("Cat meows")
        
c = Cat()
c.eat()
c.meow()

d = Dog()
d.eat()
d.bark()