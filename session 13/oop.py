# class Student:
#     def __init__(self, student_name, student_age, student_gender, student_department, student_status):
#         self.name = student_name
#         self.age = student_age
#         self.gender = student_gender
#         self.department = student_department
#         self.status = student_status


#     def __str__(self):
#         return f"{self.name} \n{self.age} \n{self.gender} \n{self.department}"

# s1 = Student("Amir", 25, "male", "Science", "active")

# print(s1)

from classes import Student, Course, BankAccount, Teacher


t1 = Teacher("Wahid", 26, "male", "Visiting Faculty")

print(t1)

s1 = Student("Amir", 25, "male", "Science", "active")
print(s1)
# c1 = Course("Java", "01.08.2025", "01.12.2025")

# s1.update_name("Ali")

# print(c1)

# s1.update_status("Suspended")
# print(s1)

# my_account = BankAccount("Bilal", 200)
# my_account.show_balance()

# my_account.update_balance(800)
# my_account.show_balance()




# how to decide which one are classes in a system
# Tips:
#    Nouns ====> Classes
#.   Verbs ====> methods/functions
#.   adjective ===> properties/fields








