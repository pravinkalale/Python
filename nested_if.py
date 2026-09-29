# age = 17

# if age >= 18:
#     if age >= 21:
#         print("Eligible")
#     else:
#         print("Not eligible")
# else: 
#     print("Minor")
    
num = int(input("Enter any number: "))

if num > 0:                            #outer if
    print("positive number")
    if num%2==0:                       #inner if
        print(num,"is even number")
    else:                              #inner else
        print(num,"is odd number")
else:                                  #outer else
    print("Negative number")
    