#input - 123
# output - 6

#input - 234
#output - 24

sum = 0
num = int(input("Enter a number: "))

while num > 0:
    rem = num % 10
    num = num // 10
    sum = sum + rem
print(sum)
    
num = int(input("Enter a number: "))
mul = 1
while num>0:
    rem = num % 10
    num = num // 10
    mul = mul * rem
print(mul)