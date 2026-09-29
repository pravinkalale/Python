# marks grading (1)

marks = float(input("Enter your Marks: "))

if marks >= 85 and marks <= 100:
    print("A+ GRADE")
elif marks >= 75 and marks <= 84:
    print("A GRADE")
elif marks >= 60 and marks <= 74:
    print("B+ GRADE")
elif marks >= 45 and marks <= 59:
    print("B GRADE")
elif marks >= 35 and marks <= 44:
    print("C GRADE")
else: 
    print("Fail")