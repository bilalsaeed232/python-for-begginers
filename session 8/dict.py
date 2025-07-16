#          0        1        2       3
# names = ["umar", "hasaan", "ali", "sudais"]
# print(names[2])


# for name in names:
#     print(name)


# account:
#   --> username
#   --> email
#   --> password
#   --> age
#   --> gender



# Programming Concept: Dictionary (in python)
# format-->  {
# key: { 
#   key: value, 
#   key: value 
#   } 
# }
users = { 
    "umar": { "username": "umar123", "email": "umar@gmail.com", "password": "123", "age": 28, "gender": "male" }, 
    "hasaan": { "username": "hasaan123", "email": "hasaan@gmail.com", "password": "hasaan122", "age": 22, "gender": "male" }, 
    }
# print(users["umar"]["username"])  ----> umar123
# print(users["umar"]["password"])  ----> 123
# print(users["hasaan"]["age"])


# conditional statements: and, or, not
# e.g if marks < 90 and marks > 80:
#         print("grade A")
# login system
# username = input("Enter your username:")
# password = input("Enter your password:")
# if users["umar"]["username"] == username and users["umar"]["password"] == password:
#     print("Login Succesfull!")
# else:
#     print("Invallid username or password")


# users.items() ===> key,value (pair)
# using for loop with dictionary
# for key, value in users.items():
#     print(key.upper(), "=====>", value["email"])


# new_email = input("enter new email:")
# new_username = input("enter new username:")
# # change values in dictionary
# # users["umar"]["age"] = 25
# users["umar"]["email"] = new_email
# users["umar"]["username"] = new_username


# print(users)


# add new items in a dictionary
# print("<<<Add a new user>>>")
# name = input("enter name:")
# username = input("enter username:")
# email = input("enter email:")
# password = input("enter password:")
# age = input("enter age:")
# gender = input("enter gender:")


# # users["ali"] = {}
# users[name] = { "username": username, "email": email, "password": password, "age": age, "gender":gender }

username = input("enter username:")
# # using for loop with dictionary
for key, value in users.items():
    # print(key.upper(), "=====>", value)
    if value["username"] == username:
        print(value["email"])



# users.pop("hasaan")

# # using for loop with dictionary
# for key, value in users.items():
#     print(key.upper(), "=====>", value)