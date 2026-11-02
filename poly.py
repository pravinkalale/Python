# class Test:
#     def m1(self):
#         print('no-arg method')
#     def m1(self,a):
#         print('one arg method')
#     def m1(self,a,b):
#         print('two-arg method')
        
# t = Test()
# # t.m1()
# # t.m1(10)
# t.m1(10,20)

"""demo program with default Arguments"""

class Test:
    def sum(self, a=None, b= None, c=None):
        if a!= None and b!= None and c!= None:
            print("The Sum of 3 Numbers:",a+b+c)
        elif a!= None and b!= None:
            print("The Sum of 2 Numbers:",a+b)
        else:
            print("Please provide 2 or 3 arguments")
            
t = Test()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10)