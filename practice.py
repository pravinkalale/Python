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

# s = input("Enter string: ").lower()   # convert to lower case

# s = s.replace(" ","")                 # avoid spaces
# rev = (s[::-1])

# if s == rev:
#     print("string palindrome")
# else:
#     print("string not palindrome")

"""Count vowels in a string."""

# s = input("Enter string:")

# count = 0
# consonant_count = 0
# for ch in s:
#     if ch in "aeiou,AEIOU":
#         count += 1
#         print(ch)
#     elif ch in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
#         consonant_count += 1
# print("total vowels:",count)
# print("consonants:",consonant_count)

"""Find the second-largest element in a list."""

# l = [29,33,22,99,44,10,35]

# largest = 0
# second_largest = 0

# for i in l:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif i > second_largest and i != largest:
#         second_largest = i
        
# print(largest)
# print(second_largest)


"""Check whether two strings are anagrams."""

"""Using Sorted"""

# str1 = input("Enter first string:")
# str2 = input("Enter second string:")

# if sorted(str1) == sorted(str2):
#     print("Given Strings are anagrams")
# else:
#     print("Given Strings are not anagrams")
    

"""Without built in function"""

# str1 = input("Enter first String:")
# str2 = input("Enter second String:")

# if len(str1) != len(str2):
#     print("Not anagram")
    
# else:
#     for i in str1:
#         if str1.count(i) != str2.count(i):
#             print("Not anagram")
#             break
#     else:
#         print("Given strings are anagram")
             
             
"""string practice"""

# s = input("Enter a string:")

# freq = {}

# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
        
# for ch in s:
#     if freq[ch] == 1:
#         print("first non repeating character:",ch)
#         break
# else:
#     print("No one-repeating character found")


"""Remove duplicate elements from a list."""

# l = [10,20,30,50,80,70,60,30,20]

# new_list = []

# for i in l:
#     if i not in new_list:
#         new_list.append(i)
        
# print(new_list)


"""Find the frequency of each character in a string."""

# s = input("Enter string:")

# for i in s:
#     count = 0
    
#     for j in s:
#         if i == j:
#             count += 1
    
#     print(i,"=", count)


"""Find common elements between two lists."""

# list = [10,20,30,40,50]

# list1 = [30,40,50,60,70]

# new_list =[]

# for i in list:
#     if i in list1:
#         new_list.append(i)
        
# print("Common Elements:",new_list)


"""Create a function to check Armstrong number."""

def armstrong():
    
    num  = int(input("Enter a number:"))
    
    sum = 0 
    temp = num
    power = len(str(num))
    
    while(num > 0):
        rem = num % 10
        sum = sum + rem**power
        num = num // 10
        
    if temp == sum:
        print("armstrong number")
    else:
        print("Not armstrong number")

armstrong()
    
       
