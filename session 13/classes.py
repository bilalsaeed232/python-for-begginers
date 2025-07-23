# Inheritance: a child class can inherit from a parent class

from random import random
from math import floor

class Person:
    def __init__(self, student_name, student_age, student_gender):
        self.name = student_name
        self.age = student_age
        self.gender = student_gender
        self._id = floor(random() * 200)
        print("Person constructor called!!")


    def update_name(self, name):
        self.name = name

    def __str__(self):
        return f"{self._id}: {self.name}, {self.age}, {self.gender} ----"



class Student(Person):
    def __init__(self, name, age, gender,student_department, student_status):
        super().__init__(name, age, gender)
        self.department = student_department
        self.__status = student_status

    def __str__(self):
        return f"{super().__str__()} {self.department} {self.__status}"


    def update_status(self, new_status):
        self.__status = new_status


class Teacher(Person):
    def __init__(self, name, age, gender, faculty):
        super().__init__(name, age, gender)
        self.__faculty = faculty

    def update_faculty(self, faculty):
        self.__faculty = faculty

    def __str__(self):
        return f"{super().__str__()}, {self.__faculty}"


    


class Course:
    def __init__(self, title, start_date, end_date):
        self.title = title
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"Title: {self.title}\nStart Date:{self.start_date}\nEnd Date: {self.end_date}"
    





# we can also restrict access to some properties
class BankAccount:
    def __init__(self, account_name, balance):
        self.__balance = balance
        self.account_name = account_name

    def show_balance(self):
        print(self.__balance)

    def update_balance(self, new_balance):
        if new_balance < 0:
            print("balance cannot be negative!")
            return
        self.__balance = new_balance




