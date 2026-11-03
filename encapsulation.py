# # private members

# class Rectangle:
#     __length = 0 
#     __breadth = 0 
    
#     def __init__(self):
#         self.__length = 5
#         self.__breadth = 3
        
#         print(self.__length)
#         print(self.__breadth)
        
# r = Rectangle()

"""Public members"""

# class employee:
#     def __init__(self, name, id):
#         self.name=name
#         self.id = id

# e = employee("abc",101)
# print(e.name)
# print(e.id)

"""Protected method"""

class Shape:
    _length = 10
    _breadth = 20
    
class Circle(Shape):
    def __init__(self):
        print(self._length)
        print(self._breadth)
        
cr = Circle()
print(cr._length)
print(cr._breadth)