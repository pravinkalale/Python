# # 1) vowels count 

# s = "programming"
# count = 0
# for ch in s:
#     if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
#         count += 1
# print("Total count is :- ",count)


# # 2) print vowels in string

# s = "programming"
# for ch in s:
#     if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
#         print("Total vowels is :- ",ch) 
        
        
# ## 3) Count Spaces in a String

# s = "python is programming lang"
# count = 0

# for ch in s:
#     if ch == ' ':
#         count += 1
# print("Total spaces are: ",count)


# ## 4)  Count the Occurrences of a Particular Character

# s = "programming"
# count = 0

# for ch in s:
#     if ch == "m":
#         count += 1
# print("Total count is: ",count)


# ## 5) to check the given string is anagram or not.

# a = input("Enter first string: ")
# b = input("Enter Second string: ")

# if len(a) != len(b):
#     print("Not Anagram")
# else:
#     for i in a:
#         count1 = 0
#         count2 = 0
        
#         for j in a: 
#             if i == j:
#                 count1 += 1
        
#         for k in b:
#             if i == k:
#                 count2 += 1
        
#         if count1 != count2:
#             print("Not Anagram")
#             break
        
#     else:
#         print("Anagram")


## 6) to reverse a given string e.g Python

## with slicing
# a = "Python"

# b = a[: : -1]
# print(b)

# a = "python"
# b = ""

# ## without slicing 
# for i in a:
#     b = i + b
# print(b)

## 7) "hello how are you" reverse a string  

# a = "hello how are you"
# b = ""
# word = ""

# for i in a:
#     if i != " ":
#         word = word + i
#     else:
#         b = word + " " + b
#         word = ""

# b = word + " " + b
# print(b[:-1])

## 8) Krishna : output : k|r|i|s|h|n|a|

# a = "krishna"

# for i in a:
#     print(i,end="|")
    
    
# 9) count a frequency of given string : Programming 

a = "Programming"
for i in a:
    count = 0
    
    for j in a:
        if i == j:
            count += 1
            
    print(i,count)