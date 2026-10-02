num = int(input("Enter Number: "))
sum = 0
temp = num

while num > 0:
    rem = num % 10        
    sum = sum + rem**3
    num = num // 10
if temp == sum: 
    print("Given number is Armstrong number!")
else:
    print("Given number is not Armstrong number!")