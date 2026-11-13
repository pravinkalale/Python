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


# """Hierarchical Inheritance"""

# class Animal:
#     def eat(self):
#         print("Animal can eat")
        
# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")
        
# class Cat(Animal):
#     def meow(self):
#         print("Cat meows")
        
# c = Cat()
# c.eat()
# c.meow()

# d = Dog()
# d.eat()
# d.bark()

"""Hybrid Inheritance"""

# class Animal:
#     def eat(self):
#         print("Animal eating")
        
# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")
        
# class Cat(Animal):
#     def meow(self):
#         print("Cat meow")
        
# class Pet(Dog, Cat):
#     def play(self):
#         print("Pet plays")
        
# p = Pet()
# p.eat()
# p.bark()
# p.meow()
# p.play()

"""Abstraction"""

# from abc import ABC , abstractmethod

# class Animal(ABC):
    
#     @abstractmethod
#     def sound(self):
#         print("Sound of Animal")
    
# class Dog(Animal):
#     def sound(self):
#         print("Dog is barking")
        
# class Cat(Animal):
#     def sound(self):
#         print("cat meow")
        
# d = Dog()
# d.sound()

# c = Cat()
# c.sound()



"""Another example"""

# from abc import ABC, abstractmethod

# #Abstract class 
# class Vehicle(ABC):
    
#     @abstractmethod
#     def start(self):
#         pass
    
#     def stop(self):
#         print("Vehicle stopped")
        
# # Child class
# class Car(Vehicle):
#     def start(self):
#         print("Car starts with a key")
        
# # Another child class
# class Bike(Vehicle): 
#     def start(self):
#         print("Bike starts with a button")
        
# # creating object
# c = Car()
# c.start()
# c.stop()

# b = Bike()
# b.start()
# b.stop()


"""Encapsulation"""

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
        
#     def deposit(self, amount):
#         self.__balance += amount
#         print("Amount Deposited:",amount)
#         print("Total Balance:",self.__balance)
        
#     def withdrow(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print("Amount Withdrawn:",amount)
#         else:
#             print("Insufficient Balance")
    
#     def check_balance(self):
#         print("Current Balance:",self.__balance)
        
# account = BankAccount(5000)
# account.check_balance()  
# account.deposit(1000) 
# account.check_balance()   
# account.withdrow(4000)  
# account.check_balance()


"""Employee Management System"""

# class Employee:
#     def __init__(self, name, id, salary):
#         self.name = name
#         self._emp_id = id
#         self.__salary = salary
        
#     def emp_name(self):
#         print("Employee Name:",self.name)
        
#     def id(self):
#         print("Employee ID:",self._emp_id)
        
#     def salary(self):
#         print("salary:",self.__salary)
        
#     def upd_salary(self, amount):
#         self.__salary += amount
#         print("Updated salary:",self.__salary)
        

# e = Employee(
#     "Pravin",
#     101,
#     30000
# )
# e.emp_name()
# e.id()
# e.salary()
# e.upd_salary(5000)


"""Polymorphism"""

class Car: 
    def start(self):
        print("Car starts with a key")
        
class Bike:
    def start(self):
        print("Bike starts with a button")
        
class Airplane:
    def start(self):
        print("Airplane engine starts")
        
c = Car()
b = Bike()
a = Airplane()

c.start()
b.start()
a.start()