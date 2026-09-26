age = int(input("Enter your Age: "))

if age >= 18:
    print("You are eligible for vote!")
else:
    print("You are not eligible for vote!")
    
    
marks = float(input("Enter your marks: "))

if marks >= 85:
    print("GRADE A+")
elif marks >= 75:
    print("GRADE A")
elif marks >= 60:
    print("GRADE B+")
elif marks >= 45:
    print("GRADE B")
elif marks >=35:
    print("GRADE C")
else:
    print("Fail")