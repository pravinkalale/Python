class Calculation1:
    def Summation(self,a,b):
        return a + b;
    
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
    
class Derived(Calculation1,  Calculation2):
    def Divide(self,a,b):
        return a/b;
    
d = Derived()
# print(d.Summation(10,20))
# print(d.Multiplication(10,20))
# print(d.Divide(10,20))

"""issubclass method used"""

# print(issubclass(Derived,Calculation2))          
# print(issubclass(Calculation1,Calculation2))

"""is instance method """

print(isinstance(d,Derived))