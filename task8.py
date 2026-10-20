# employees = [
#     {"id": 101, "name": "Amit", "salary": 50000},
#     {"id": 102, "name": "Rahul", "salary": 75000},
#     {"id": 103, "name": "Priya", "salary": 65000}, 
# ]

# result = {}

# for emp in employees:
#     result[emp["id"]] = emp
    
# print(result)


a = 7
b = 2
if a*b >= 10:
    print("Big")
else:
    print("small")
    
    
import calendar
year = int(input("ENTER YEAR: "))
month = int(input("ENTER MONTH: "))

print("\n",calendar.month(year,month))