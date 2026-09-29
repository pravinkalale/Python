# # marks grading (1)

# marks = float(input("Enter your Marks: "))

# if marks >= 85 and marks <= 100:
#     print("A+ GRADE")
# elif marks >= 75 and marks <= 84:
#     print("A GRADE")
# elif marks >= 60 and marks <= 74:
#     print("B+ GRADE")
# elif marks >= 45 and marks <= 59:
#     print("B GRADE")
# elif marks >= 35 and marks <= 44:
#     print("C GRADE")
# else: 
#     print("Fail")

# # positive or negative (2)

# num = int(input("Enter a number: "))

# if num > 0: 
#     print(num,"is positive")
# elif num < 0:
#     print(num,"is negative")
# else: 
#     print(num,"is zero")

# # even odd & special (3)

# num = int(input("Enter a number: "))

# if num == 0:
#     print(num,"is zero")
# elif num % 2 == 0:
#     print(num,"is even")
# else: 
#     print(num,"is odd")

# # Age category (4)

# age = int(input("Enter your age: "))

# if age >= 0 and age <= 12:
#     print("child")
# elif age >= 13 and age <= 19:
#     print("Teenager")
# elif age >= 20 and age <= 59:
#     print("Adult")
# else: 
#     print("Senior Citizen")

# # Temperature check (5)

# temperature = float(input("Enter Temperature: "))

# if temperature < 15:
#     print("Temperature is Cold")
# elif temperature >= 15 and temperature <= 25:
#     print("Temperature is Normal")
# elif temperature >= 26 and temperature <= 35:
#     print("Temperature is warm")
# else:
#     print("Temperature is Hot")

# # Electricity Bill (6)

# unit = int(input("Enter electricity units: "))

# if unit > 0 and unit <= 100:
#     print("Electricity Bill = ₹",unit*5)
# elif unit >= 101 and unit <= 200:
#     print("Electricity Bill = ₹",unit*7)
# elif unit >= 201 and unit <= 300:
#     print("Electricity Bill = ₹",unit*10)
# else:
#     print("Electricity Bill = ₹",unit*12)

# # Salary Bonus (7)

# salary = int(input("Enter salary: "))

# if salary < 20000:
#     print("Bonus:", salary*5/100)
# elif salary >= 20000 and salary <= 40000:
#     print("Bonus:", salary*10/100)
# elif salary >= 40001 and salary <= 60000:
#     print("Bonus:", salary*15/100)
# else: 
#     print("Bonus:", salary*20/100)

# # Percentage division (8)

# percentage = float(input("Enter Percentage: "))

# if percentage >= 75:
#     print("Distinction")
# elif percentage >= 60 and percentage <= 74:
#     print("First Class")
# elif percentage >= 50 and percentage <= 59:
#     print("Second Class")
# elif percentage >= 35 and percentage <= 49:
#     print("Pass Class")
# else:
#     print("Fail")

# # BMI Category (9)

# weight = int(input("Enter Weight: "))
# height = float(input("Enter Height: "))

# BMI = weight / (height*height)

# if BMI < 18.5:
#     print("Underweight")
# elif BMI >= 18.5 and BMI <= 24.9:
#     print("Normal")
# elif BMI >= 25 and BMI <= 29.9:
#     print("Overweight")
# else:
#     print("Obese")

# shopping discount (10)

amount = float(input("Enter shopping amount: ")) 
    
if amount < 1000:
    print("No Discount")
elif amount >= 1000 and amount <= 4999:
    print("Discount:₹", amount*5/100)
    print("Final Amount:₹", amount - (amount*5/100))
elif amount >= 5000 and amount <= 9999:
    print("Discount:₹", amount*10/100)
    print("Final Amount:₹", amount - (amount*10/100))
else: 
    print("Discount:₹", amount*15/100)
    print("Final Amount:₹",amount-( amount*15/100))