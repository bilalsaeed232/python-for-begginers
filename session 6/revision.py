# print name on the screen
# builtin function in python: print
# print("Bilal....")



# variables and constants
# e.g x = a + b
# x = 5
# n = 23
# name = "umar"
# n = 70

# data types
# number ===> 'int'
# string/text ===> 'str'


# builtin function in python: input
# name = input("Enter your name: ")

# print(name)


# print("Enter your name:")



# ask your name and print following:
# Welcome, [name]

# n = input("Enter your name:")
# print("Welcome",n)


# So Far we covered:
# print()
# input()
# variables & constants

########################################################

# if else statements


# always true
# if 5 == 5:
#     print("what is this")
#     print("Hello world")
#     print("byeeee")
# else:
#     print("Helooooooo")


# conditonal operators:
# equal comparison: ==
# greater than comparison: >
# less than comparison: <
# n = 45
# if n > 50:
#     print("n is greater than 5")
# elif n > 40:
#     print("n is greator than 40")
# elif n > 30:
#     print("n is greator than 30")
# else:
#     print("no condtion is true")




# e.g grading system
# 90+ ===> A+
# 80+ ===> A
# 70+ ===> B
# 60+ ===> C
# 50+ ===> D
# other Fail


# marks = input("Enter your marks:")
# marks = int(marks)
# if marks > 90:
#     print("Grade A+")
# elif marks > 80:
#     print("Grade A")
# elif marks > 70:
#     print("Grade B")
# elif marks > 60:
#     print("Grade C")
# elif marks > 50:
#     print("Grade D")
# else:
#     print("Fail")


########################################

# LOOPS: programming concept

# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")

# range of numbers: range(5) =====> [0,1,2,3,4]
# similar to builtin functions we covered so far: print(), input()

# for i in range(5):
#     print(i, "Hello World")


# table of 2:
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20

# print("2 x 1 = 2")
# print("2 x 2 = 4")
# print("2 x 3 = 6")
# print("2 x 4 = 8")
# print("2 x 5 = 10")
# print("2 x 6 = 12")
# print("2 x 7 = 14")
# print("2 x 8 = 16")
# print("2 x 9 = 18")
# print("2 x 10 = 20")

# num = 15
# for i in range(1, 11): # [1,2,3,4,5,6,7,8,9,10]
#     n = i * num
#     # print(x)
#     print(num, "x", i, "=", n)


num = input("Enter a number:")
num = int(num)
for i in range(1, 11): # [1,2,3,4,5,6,7,8,9,10]
    n = i * num
    # print(x)
    print(num, "x", i, "=", n)








