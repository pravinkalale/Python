# class student:
#     name = 'pravin kumar'
    
# s1 = student()
# print(s1.name)

# class Animal:
#     def sound(self):
#         print('hahaaha')
        
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
        
# class Cat(Animal):
#     def meow(self):
#         print("Cat meow")
        
# c = Cat()
# c.meow()
# c.sound()

# d = Dog()
# d.bark()
# d.sound()


# s = Animal()
# s.sound()

"""11/11/26"""

"""Check whether a number is even or odd."""

# a = int(input("Enter a Number: "))

# if a%2==0:
#     print("Even number")
# else:
#     print("Odd number")

"""Find the largest of three numbers."""

# a = int(input("Enter first Number: "))
# b = int(input("Enter second Number: "))
# c = int(input("Enter third Number: "))

# if a > b and a > c:
#     print(a,"is largest")
# elif b > a and b > c:
#     print(b,"is largest")
# elif c > a and c > b: 
#     print(c,"is largest")
# else:
#     print("All of same")

"""Create a class Student with name and marks."""

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        
#     def score(self):
#         print(self.name)
#         print(self.marks)
        
# S1= Student("gaju",66)
# S1.score()

"""Reverse a string without using built-in functions."""

# s = "Hello"

# print(s[::-1])

"""Check whether a number is prime."""

# num = int(input("Enter a Number: "))

# if num > 1:
#     for i in range(2,num):
#         if num % i == 0:
#             print("Not prime number")
#             break
#     else:
#         print("Prime number")
# else:
#     print("not prime number")

"""Single Inheritance"""

# class Animal:
#     def eat(self):
#         print("Animal is eating")
        
# class Dog(Animal):
#     def bark(self):
#         print("Dog is Barking")

# d = Dog()
# d.eat()
# d.bark() 

"""Multilevel Inheritance"""

# class Grandfather:
#     def house(self):
#         print("Grandfather's House")

# class Father(Grandfather):
#     def car(self):
#         print("Father's car")
        
# class Son(Father):
#     def bike(self):
#         print("Son's Bike")
        
# s = Son()
# s.house()
# s.car()
# s.bike()

"""using super()"""

# class Parent:
#     def show(self):
#         print("parent class")
        
# class Child(Parent):
#     def show(self):
#         super().show()
#         print("Child class")

# obj = Child()
# obj.show()



# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
        
# class Developer(Employee):
#     def __init__(self, name, salary, language):
#         super().__init__(name,salary)
#         self.language = language
        
#     def display(self):
#         print("Name:", self.name)
#         print("salary:", self.salary)
#         print("language:", self.language)

# obj = Developer("Pravin",25000,"Python")
# obj.display()


"""Find factorial of a number."""

# num = int(input("Enter a number: "))

# fact = 1
# for i in range(1, num + 1):
#     fact = fact * i
# print("factorial:", fact)


"""Check whether a string is palindrome."""

s = input("Enter string: ").lower()   # convert to lower case

s = s.replace(" ","")                 # avoid spaces
rev = (s[::-1])

if s == rev:
    print("string palindrome")
else:
    print("string not palindrome")