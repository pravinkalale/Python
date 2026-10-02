num = int(input("Enter any number: "))
sum =0
temp = num

while(num>0):
    rem=num%10
    sum=sum+rem**3 
    num=num//10
print("reverse number is: ",sum)
if(temp==sum):
    print("given number is Armstrong number")
else:
    print("given number is not Armstrong number")