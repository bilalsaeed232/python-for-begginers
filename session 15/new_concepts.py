
### print("="*40)

# print("-"*50)
# print("Account information")
# print("-"*50)

# print("Name: Bilal")
# print("Gender: Male")




### input("enter a number").strip()
# name = input("Enter your name:")
# name = name.strip()
# print(name)

# if name == "bilal":
#     print("Name is Bilal")
# else:
#     print("Name is not Bilal")



### __name__ == "__main__"
# print(__name__)

# file1: library/classes (e.g Amazon classes - Customer, Product) <---- user defined modules
# file2: uses this library/classes (i.e file1) <------- import thoses clasess as modules

#--------------------------------------------

# Real life example
# Facebook
## classes: User, Friend, Feed. (facebook_classes.py)
## login.py: User (username, password) <----- from facebook_classes.py import User 






# try ... except



# while True:
#     print("-"*50)
#     print("1. Display Restaurant Menu")
#     print("2. Order Food")
#     print("0. exit")
#     print("-"*50)
#     try:
#         choice = int(input("enter first number:"))

#         match choice:
#             case 1:
#                 print("Biryani")
#                 print("Karahi")
#                 print("Qorma")
#             case 2:
#                 print("Ordering foood")
#             case 0:
#                 print("Byee")
#                 break
#     except:
#         print("Enter a valid number")



# conditional expression or ternary operator
# marks = int(input("enter your marks:"))
# total_marks = 600

# # anjaam = supra_dabalay/bachat_osho
# anjaam = "unknown"
# anjaam = "supra_dabalay" if marks < total_marks - 10 else "bachat_osho"
# # if marks < total_marks - 10:
# #     anjaam = "supra_dabalay"
# # else:
# #     anjaam = "bachat_osho"

# print(anjaam)





### list comprehension
# nums = []
# for i in range(1, 21):
#     nums.append(i)

# nums = [i for i in range(1, 21)]


# conditional expression + list comprehensions
# for i in range(1, 21):
#     if i == 6:
#         nums.append("SIX")
#     else:
#         nums.append(i)

# nums = ["SIX" if i == 6 else i for i in range(1, 21)]
# nums = [i for i in range(1, 21) ]

# nums = []
# for i in range(1, 21):
#     if i%2==0:
#         nums.append(i)



nums = ["TEN" if i==10 else i for i in range(1, 21) if i%2==0]
# nums = [i for i in range(1, 21) if i==10]
print(nums) # [1,2,3,4,5,6...20]
