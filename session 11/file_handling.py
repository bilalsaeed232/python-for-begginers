# File Handling in Python

# how to work with files in python

# i want to print data from my text file

# 1. Read from file
# file = open("data.txt")

# line1 = file.readline()

# print(line1)

# line2 = file.readline()
# print(line2)


# # file = open("data.txt")
# line3 = file.readline()
# print(line3)

# line4 = file.readline()
# print(line4)

# file.close()


# file = open("data.txt")
    

# with open("data.txt") as file:
#     for line in file.readlines(): # ["1. the quick brown fox jumps over the lazy dog. ", "2. the quick brown fox jumps over the lazy dog."....]
#         print(line)

# l = file.readline()

# print(l)


# 2. Write to a file
# my_line = "\n7. blablablab"
# with open("files/data.txt", "a") as file:
#     file.writelines(my_line)


student_names = ["\numar", "\namir", "\nsudais", "\nhasaan"]
with open("files/data.txt", "a") as file:
    file.writelines(student_names)









