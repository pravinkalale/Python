# print 1 to 10 numbers

# i = 1
# while(i<=10):
#     print(i)
#     i+=1

# reverse print
    
# i = 10
# while(i>=1):
#     print(i)
#     i-=1

# print reverse number of user input

num = int(input("Enter Number: "))

rev = 0

while (num>0):
    rem = num%10       # reminder
    rev = rev*10+rem
    num = num//10       #quation 
print(rev)