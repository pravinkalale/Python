class Student:
    def __init__(self, name, age, marks):
        self.name = name      
        self.age = age            #instance variables
        self.marks = marks
        
    def talk(self):      # instance method
        
        print("Hello my Name is :",self.name)
        print("my age is :",self.age)
        print("my marks are :",self.marks)
        
s = Student("bhranti",18,80)
s.talk()