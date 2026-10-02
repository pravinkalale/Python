# print repeated numbers count

num = int(input("Enter a Number: "))
num2 = int(input("Enter count number: "))
count = 0

while num > 0:
    rem = num % 10
    num = num // 10
    if rem == num2:
        count = count + 1
print(count)

            
#Print unique values count
         
num = int(input("Enter Number: "))

temp = num
unique = 0

while temp > 0:

    rem = temp % 10
    temp = temp // 10

    count = 0
    check = num

    while check > 0:

        digit = check % 10
        check = check // 10

        if rem == digit:
            count = count + 1

    if count == 1:
        unique = unique + 1

print("Unique values:", unique)
        