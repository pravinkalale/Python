# def pali(p):
#     return p == p[::-1]

#Armstrong number 

def armstrong(num):
    if num < 0:
        return False

    digits = str(num)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return num == total