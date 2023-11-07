from datetime import date


class Person:
    first_name = ""
    second_name = ""
    birth = date
    address = ""
    phone_num = int

    def change_phone_num(self, new_num):
        self.phone_num = new_num

    def change_address(self, new_address):
        self.address = new_address


class Student(Person):
    group = ""
    marks_list = [{str: [int, date]}]
    parents = [Person]
    food_allergy = []

    def change_group(self, new_group):
        self.group = new_group

    def add_mark(self, subject, mark, current_date):
        self.marks_list.append({subject: [mark, current_date]})


class Teacher(Person):
    salary = float
    graduation = ""
    subject = ""

    def change_salary(self, new_salary):
        self.salary = new_salary

    def add_graduation(self, new_graduation):
        self.graduation = new_graduation

    def change_subject(self, new_subject):
        self.subject = new_subject
