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

class Student:
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("adding new student in database..")
        
s1 = Student("Pravin", 98)
print(s1.name, s1.marks)

s2 = Student("shradha didi",76)
print(s2.name, s2.marks)