# # Q1. Create a list containing 5 numbers and print it.

# l = [10,20,30,40,50]

# print(l)

# # Q2. Create a list containing your name, age, city and course.

# l = ["Pravin",23,"Nanded","MCA"]

# print(l)

# # Print 10, 30 aur 50 using indexing.

# l = [10,20,30,40,50]

# print(l[0])
# print(l[2])
# print(l[4])

# # Q4. Using the same list, print 50, 40 and 20 using negative indexing.

# l = [10,20,30,40,50]

# print(l[-1])
# print(l[-2])
# print(l[-4])

# Change 20 to 200.

# l = [10, 20, 30, 40]

# l[1]= 200

# print(l)

# list practices 3/11/26

# find elements in even index

# a = [2,1,4,3,5,7,8,9,3]
# # for i in range(len(a)):
# #     if(i%2 == 0):
# #         print(a[i])

# # find even elements

# # for i in a:
# #     if(i%2==0):
# #         print(i)

# # remove duplicates elements from the list
# a = [2,1,2,4,3,5,1,5,4,3,3]
# list2 =[]

# for i in a:
#     if i not in list2:
#         list2.append(i)
# print(list2)
       
       
# to add elements in empty list using user input
# find minimum elements in a given list without using min()
# max elements in given list without using max()
# addition of two lists using for loop and using list comprehension also
# sort the elements in ascending order without sort() method

# to add elements in empty list using user input

# my_list = []

# n = int(input("Enter number of elements: "))

# for i in range(n):
#     num = int(input("Enter number: "))
#     my_list.append(num)

# print("list",my_list)

# find minimum elements in a given list without using min()

l = [2,4,5,6,7,9,23,3]

smallest = l[0]

for i in l:
    if i < smallest:
        smallest = i

print("Smallest:", smallest)