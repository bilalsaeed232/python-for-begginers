# Write e program that I can use as a daily journaling

# Project name: Brain Dump

from datetime import datetime

time_stamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

# print(time_stamp)
entry = input("What is in your mind today: ")

with open("journal.txt", "a") as file:
    file.write(time_stamp)