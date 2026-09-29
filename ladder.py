# marks = float(input("Enter your marks: "))

# if marks >= 90 and marks <= 100:
#     print("A+ GRADE")
# elif marks >= 80 and marks <= 90:
#     print("B+ GRADE")
# elif marks >= 65 and marks <= 80:
#     print("C+ GRADE")
# elif marks >= 35 and marks <= 65:
#     print("D+ GRADE")
# else: 
#     print("Failed")
    
    
# greatest number 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print(a,"is greater")
elif b > a and b > c:
    print(b,"is greater")
elif c > a and c > b:
    print(c,"is greater")
else:
    print("all of same")