#vowels
# s = "programming"
# count = 0
# for ch in s:
#     if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
#         count += 1
# print("Total count is :- ",count) 


# Count Total Characters in a String

# s = "programming"
# count = 0

# for ch in s:
#     count += 1

# print("Total characters are :-", count)


# Count the Occurrences of a Particular Character


s = "programming"
count = 0

for ch in s:
    if ch == 'a':
        count += 1

print("Total count is :-", count)


# Count Spaces in a String

s = "python is programming lang"
count = 0

for ch in s:
    if ch == ' ':
        count += 1

print("Total spaces are :-", count)



# Convert a String into Uppercase


# s = "programming"
# result = ""
# for ch in s:
#     if ch >='a' and ch <= 'z':
#         result += chr(ord(ch)  - 32)
#     else:
#         result +=ch

# print("Uppercase string is :-",result)


# #  Convert a String into Lowercase

# s = "PRAVIN"
# result = ""

# for ch in s:
#     if ch >= 'A' and ch <= 'Z':
#         result += chr(ord(ch) + 32)
#     else:
#         result += ch

# print("Lowercase string is :-", result)


# #reverse a striung

# s="pravin"
# rev = ""
# for ch in s:
#     rev = ch + rev
# print("Reverse string is :-",rev)


# ### checks  whether s string is palindrome or not

# s = "level"
# rev = ""
# for ch in s :
#     rev = ch + rev
# if s == rev :
#     print("String is palindrome")
# else :
#     print("string is not palindrome")

s1 = "mom"
s2 = s1 [: : -1]
if (s1 == s2):
    print("string is pallindrome")
else:
    print("string is not palindrome")