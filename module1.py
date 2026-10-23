# def pali(p):
#     return p == p[::-1]

#Armstrong number 

# def armstrong(num):
#     if num < 0:
#         return False

#     digits = str(num)
#     power = len(digits)
#     total = 0

#     for digit in digits:
#         total += int(digit) ** power

#     return num == total


#palindrome number

def pali(num):
    temp = num
    rev = 0
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
        if temp == rev:
            print("given number is palindrome")
        else: 
            print("given number is not palindrome")





#Armstrong number
def armstrong(num):
    temp = num
    sum = 0
    while num > 0:
        rem = num % 10
        sum = sum + rem ** 3
        num = num // 10
    if temp == sum:
        print("given number is armstrong number")
    else: 
        print("given number is not armstrong number")        