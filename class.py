# class Student:                            # creat a class 
#     def __init__(self, name, age):        # defined constructor 
        
#         self.name = name
#         self.age = age                    # instance variable
        
#     def show(self):                       # instance Method
        
#         print(self.name)                  # for print the data 
#         print(self.age)
        
# s1 = Student('Pravin',23)                 # create an a object
# s1.show()                                 # call to the method 

class Student:
    
    def __init__(self,x,y,z):
        self.name = x
        self.rollno = y
        self.marks = z
        
    def display(self):
        print("Student Name:{}\nRollno:{}\nMarks:{}".format(self.name,self.rollno,self.marks))
        
s1 = Student("Durga",101,80)
s1.display()
        