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

"""Create Account class with 2 attributes - balance & account no.
create mthods for debit, credit & printing the balance."""

class Account:
    def __init__(self,bal, acc):
        self.balance = bal
        self.account_no = acc
     
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance =", self.get_balance())
        
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance =", self.get_balance())
        
    def get_balance(self):
        return self.balance
         
acc1 = Account(10000, 14125466)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)

