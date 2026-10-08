# s = {3,6,2,8,4,7,4,9,3}
# print(s)
# s.add(99)
# print(s)
# s.remove(4)
# print(s)

s1 = {10,20,30,40}
s2 = {30,40,50,60}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.issubset(s2))
a = s1.symmetric_difference(s2)
print(a)

x = {"a","b","c"}
y = {"c","d","e"}
z = {"f","g","c"}
x.intersection_update(y,z)
print(x)