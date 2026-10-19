# t = (1,2,3)
# print(t)
# t[3]=32
# print(t)

# t = 10,20,True,"Hi",30.5,3+5j

# print(t[2])
# print(t[5])

# print(t[1:4])      #slicing 
# print(t[ : : 2])   #slicing

# l = [10,20,"Hi",3+5j]

# l = tuple
# print(l)


# t = (10,55.5,'x',True,[1,2,3],"Hii",10)
# print(t)
# print(type(t))
# t[6] = 20
# print(t)



# tuple1 = (99,2,3,4,5,8,6,6,6,6,6)
# print(len(tuple1))
# print(min(tuple1))
# print(max(tuple1))
# print(sum(tuple1))
# cnt = tuple1.count(6)
# print(cnt)
# ind = tuple1.index(2)
# print(ind)
# t = tuple(reversed(tuple1))
# print(t)
# s = tuple(sorted(tuple1))
# print(s)

# map function 

def sq(x):
    return x*x
t=(1,2,3,4,5,6,7)
ut = map(sq,t)
print(list(ut))