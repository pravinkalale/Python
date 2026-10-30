class Student:
    def __init__(self, name, age):
        
        self.name = name
        self.age = age
        
    def show(self):
        
        print(self.name)
        print(self.age)
        
s1 = Student('Pravin',23)
s1.show()