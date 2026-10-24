# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr)

# import numpy
# arr = numpy.array([1,2,3,4,5])
# print(arr)

#Types of arrays   

# import numpy as np 
# arr = np.array(33)
# arr = np.array([1,2,3,4,5])
# arr = np.array([[1,2,3],[4,5,6]])
# arr = np.array([[1,2],[3,4],[5,6],[7,8]])
# print(arr)

# import numpy as np 
# arr1 = np.array([1,2,3,4,5])
# arr2 = np.array([1,2,3,4,6.6,8.5])
# print(arr1.dtype)
# print(arr2.dtype)

# import numpy as np 
# x = np.array([3,5]) 
# y = np.array([2,5])
# print("Original numbers:")
# print(x)
# print(y)
# print("comparison - greater")
# print(np.greater(x, y))

# print("comparison - greater_equal")
# print(np.greater_equal(x,y))

# print("Comparison - less")
# print(np.less(x,y))

# print("Comparison - less_eqaul")
# print(np.less_equal(x,y))

#reshape into two dimensional array

import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
na = a.reshape(4,3)
print(na)

#convert into multidimensional

naa = a.reshape(2,2,3)
print(na)

#search element
a = np.array([1,2,3,4,5,4,4])
n = np.where(a==4)
print(n)

# #count duplicate elements

# a = np.array([1, 2, 3, 4, 5, 4, 4])

# values, counts = np.unique(a, return_counts=True)
# print(dict(zip(values, counts)))

a = np.array([1,2,3,4,5,6,7,8])
x = np.where(a%2 == 0)
print(x)

print(np.sort(a))