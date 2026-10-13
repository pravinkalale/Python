# # arrange the students list based on marks 

# students = [("Rahul",85), ("Amit",70), ("Priya",95)]

# students.sort(key=lambda x: x[1])

# print(students)

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



# check num divisible by 5 or not 

# divisible = lambda n: "Divisible by 5" if n % 5 == 0 else "Not divisible by 5"
# # print(divisible(25))

# # check login successfully or not 

username = "kalale"
correct_pass = "pravin123"
password = lambda u,p: "Login successful" if u == username and  p == correct_pass else "Invalid person"

print(password("kalale","pravin123"))
