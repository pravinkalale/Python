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

a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))
c = int(input("Enter third Number: "))

if a > b and a > c:
    print(a,"is largest")
elif b > a and b > c:
    print(b,"is largest")
elif c > a and c > b: 
    print(c,"is largest")
else:
    print("All of same")