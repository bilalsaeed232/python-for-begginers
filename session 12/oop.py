# so far we have used functions

# students = [
#     { "name": "Amir", "age": 25, "gender": "male", "department": "Managment", "status": "active"},
#     { "name": "Akhyan", "age": 15, "gender": "male", "department": "Computer Science", "status": "suspended"},
#     { "name": "Ali", "age": 35, "gender": "male", "department": "BBA"},
# ]

# search_name = input("Search student by name: ")

# for student in students:
#     if student["name"] == search_name:
#         print(student["name"])
#         print(student["age"])
#         print(student["gender"])
#         print(student["department"])


# update status: suspended
# search_name = input("Search student by name: ")

# for student in students:
#     if student["name"] == search_name:
#         student["status"] ="SUSPENDED"

# print(students)


# OOP: Object Oriented Programming
# Classes and Objects
# examples of classes:
    # Class --->  Student
    # Class --->  Person
    # Class --->  Car
    # Class --->  Animal
#Class (blueprint)
# Properties:
#   e.g  Car
#           - make
#           - model
#           - speed

# Functions:
#   start()
#   stop()
#   

# Constructor:
#   initialise properties of class


# Car blueprint ==> Class
# Actual Car ==> Object 

# House blueprint ==> Class
# Actual House # 1 (instance) ==> Object
# Actual House # 2 (instance) ==> Object
# Actual House # 3 (instance) ==> Object
#
# 
# Instance ===> current object at this moment 


# class Car:
#     def __init__(self, new_make, new_model, new_speed, new_engine):
#         self.make = new_make
#         self.model = new_model
#         self.speed = new_speed
#         self.engine = new_engine

#     def start(self):
#         print(self.make, self.engine, "Engine Started!!!")

#     def stop(self):
#         print(self.make, "Engine Stopped!!!")



# c1 = Car("Mercedes", "2019", 400, "v9")
# c2 = Car("VolksWagen", "2015", 100, "v8")
# c3 = Car("Audi", "2022", 200, "v7")

# print(c1.make)
# print(c2.make)
# print(c3.make)

# print("------------------")

# c1.start()
# c1.stop()

# c2.start()
# c2.stop()

# c3.start()
# c3.stop()



# Lets replicate our original students problem


# students = [
#     { "name": "Amir", "age": 25, "gender": "male", "department": "Managment", "status": "active"},
#     { "name": "Akhyan", "age": 15, "gender": "male", "department": "Computer Science", "status": "suspended"},
#     { "name": "Ali", "age": 35, "gender": "male", "department": "BBA"},
# ]

# for student in students:
#     if student["name"] == search_name:
#         print(student["name"])
#         print(student["age"])
#         print(student["gender"])
#         print(student["department"])

class Student:
    def __init__(self, student_name, student_age, student_gender, student_department, student_status):
        self.name = student_name
        self.age = student_age
        self.gender = student_gender
        self.department = student_department
        self.status = student_status

    def show(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.department)
        print(self.status)


    def update_status(self, new_status):
        self.status = new_status


# s1 = Student("Amir", 25, "male", "Science", "active")
# s2 = Student("Akhyan", 15, "male", "Computer Science", "suspended")
# s3 = Student("Ali", 35, "male", "BBA", "inactive")


# s1.show()
# print('-----------')
# s2.show()


print('=========================')
# print(s1.status)

# s1.update_status("Suspended")

# print(s1.status)
# print(s2.status)



# s1.update_status("ACTIVE")

# print(s1.status)


# Encapsulation ====> put all logic inside on unit i.e inside class

name = input("Enter student name:")
age = input("Enter student age:")
gender = input("Enter student gender:")
department = input("Enter student department:")

student = Student(name, age, gender, department, "active")


student.show()

new_status = input("Update student status:")
student.update_status(new_status)

print("================")
student.show()
