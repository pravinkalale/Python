# from abc import ABC, abstractmethod

# # Abstract class
# class Animal(ABC):

#     @abstractmethod            #decorator 
#     def sound(self):           #Abstract method
#         pass


# # Child class
# class Dog(Animal):

#     def sound(self):
#         print("Dog barks")


# class Cat(Animal):

#     def sound(self):
#         print("Cat meows")


# # Creating objects
# d = Dog()
# d.sound()

# c = Cat()
# c.sound()


# from abc import ABC, abstractmethod

# class Car(ABC):
    
#      @abstractmethod
#      def speed (self):
#         pass
        
# class BMW(Car):
#     def speed(self):
#         print("BMW has 250 kmph")
        
# class Audi(Car):
#     def speed(self):
#         print("Audi has 200 kmph")
        
# class Farrari(Car):
#     def speed(self):
#         print("Farrari has 300 kmph")
        
# f = Farrari()
# f.speed()

# a = Audi()
# a.speed()

# b = BMW()
# b.speed()




# from abc import ABC, abstractmethod

# class Bank(ABC):

#     @abstractmethod
#     def interest(self):
#         pass


# class SBI(Bank):
#     def interest(self):
#         print("SBI interest rate is 7%")


# class HDFC(Bank):
#     def interest(self):
#         print("HDFC interest rate is 8%")


# class ICICI(Bank):
#     def interest(self):
#         print("ICICI interest rate is 7.5%")


# s = SBI()
# s.interest()

# h = HDFC()
# h.interest()

# i = ICICI()
# i.interest()


from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def salary(self):
        pass
 

class Manager(Employee):
    def salary(self):
        print("Manager salary is 50000")


class Developer(Employee):
    def salary(self):
        print("Developer salary is 40000")


class Tester(Employee):
    def salary(self):
        print("Tester salary is 30000")


m = Manager()
m.salary()

d = Developer()
d.salary()

t = Tester()
t.salary()

