# def mygen():
#     yield 'A'
#     yield 'B'
#     yield 'C'
    
# g = mygen()
# print(type(g))

# print(next(g))
# print(next(g))
# print(next(g))

# def mygen():
#     yield 5
#     yield 4
#     yield 3
#     yield 2

# g = mygen()
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# for i in g:
#     print(i)


# def pk():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
    
# g = pk()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def simple():
#     for i in range(1,6):
#         yield i 
# r = simple()
# for g in r:
#     print(g)
    
# def simple():
#     i=1
#     while i <= 5:
#         yield i
#         i+=1
# g = simple()
# for r in g:
#     print(r)




# def simple():
#     for i in range(1, 6):
#         yield i

# r = simple()

# while True:
#     try:
#         g = next(r)
#         print(g)
#     except StopIteration:
#         break


# a = [x*x for x in range(1,1000001)]
# print(a)

#with generator

g = (x*x for x in 
     range(1000000))
print(next(g))