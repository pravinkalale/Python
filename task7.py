str = "welcome"
str2 = str.capitalize()
print(str2)

str = "WELCOME"
str2 = str.isupper()
str3 = str.lower()
print(str2)
print(str3)

str = "welcome"
str2 = str.islower()
str3 = str.upper
print(str2)
print(str3)

str = "welcome"
print(len(str))

str = "java is a programming language"

str2 = str.replace("java","python")
print(str2)

#join functions

str = ""
list = ['h','e','l','l','o']
str2 = str.join(list)
print(str2)

str = "Welcome"
str2 = str.index("c")
print(str2)

str = "communication"
str2 = str.rfind("c")
print(str2)

str = "Welcome to the python"
str2 = str.index("p",0,20)
print(str2)

#partition() function 

str = "Python is a programming language"
str2 = str.partition("a")
print(str2)

# split funtion 

str = "Python is a programming language"
str2 = str.split()
print(type(str2))
print(str2)

# count function 

str = "Hello welcome"
str2 = str.count('e')
print("occurences:",str2)

txt = "I love apples, apple is my favorite fruit"
x = txt.count("apple", 10,24)
print(x)

# find the vowels

s = "programming"
count = 0
for ch in s:
    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        count += 1
print(count)
   