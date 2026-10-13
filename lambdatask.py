
# # addition using lambda function 

# add = lambda a,b: a+b
# print(add(10,20))

# # Multiplication using lamda function 

# mul = lambda a,b: a*b
# print(mul(10,20))

# # check eligibile for vote 

# vote = lambda age: "Eligibile for vote" if age >= 18 else "Minor"
# print(vote(23))

# #Find the square of 8 using lambda.

# square = lambda x: x*x
# print(square(8))

# #Add three numbers using lambda 

# add = lambda a,b,c: a+b+c
# print(add(10,20,30))

# #Find the greatest of two numbers using lambda

# greatest = lambda a,b: a if a > b else b
# print("greatest number:",greatest(20,50))

# # check the even odd number 

# check = lambda x : "Even Number" if x % 2 == 0 else "Odd Number"
# print(check(12))
# print((check(7)))

# check num divisible by 5 or not 

# divisible = lambda n: "Divisible by 5" if n % 5 == 0 else "Not divisible by 5"
# # print(divisible(25))

# # check login successfully or not 

# username = "kalale"
# correct_pass = "pravin123"
# password = lambda u,p: "Login successful" if u == username and  p == correct_pass else "Invalid person"

# print(password("kalale","pravin123"))

# # check whether a number is zero or non zero

# zero = lambda x: "number is zero" if x == 0 else "Number is not zero"
# print(zero(5))

# #find the smaller of two numbers 

# smaller = lambda a,b : a if a < b else b
# print("Smaller number is:",smaller(80,455))

# # Check whether a number is divisible by both 5 and 10

# check = lambda x: "Divisible by 5 and 10" if x % 5 == 0 and x % 10 == 0 else "Not divisible by 5 and 10"

# print(check(79))

# # Check pass or fail. Passing marks are 35 or more

# marks = lambda M : "Pass" if M >= 35 else "Fail"
# print(marks(33))

# Check whether a number is a two-digit number (10–99)

check = lambda n : "Two digit" if n <= 99 else "this is not two digit"
print(check(10))

# # arrange the students list based on marks 

# students = [("Rahul",85), ("Amit",70), ("Priya",95)]

# students.sort(key=lambda x: x[1])

# print(students)