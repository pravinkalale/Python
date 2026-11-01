# Single inheritance with constructors

class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print(self.name ,"is speaking")

class Dog(Animal):
    def bark(self):
        print("dog is barking")
        
d = Dog("Animal")
d.bark()
d.speak()