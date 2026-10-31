class Animal:                        # parent class
    def speak(self):
        print("Animal Speaking")
        
#child class dog inherits the base class Animal

class Dog(Animal):               # child class 
    def bark(self):
        print("dog barking")
d = Dog()
d.bark()
d.speak()