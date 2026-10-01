# print reverse number of user input

num = int(input("Enter Number: "))

rev = 0

while (num>0):
    rem = num%10       # remainder
    rev = rev*10+rem
    num = num//10       #quotient 
print("reverse number is :",rev)