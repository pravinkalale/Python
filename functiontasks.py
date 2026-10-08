##using function chek the given number is palindrome or not

num=int(input("Enter a number: "))
def palindrome(num):
    temp = num
    reverse = 0

    while num>0:
        rem=num%10
        reverse=reverse*10+rem
        num=num // 10
    if temp==reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")
palindrome(num)

