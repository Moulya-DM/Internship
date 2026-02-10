# Problem Statement
# Create a program for a College Management System using Hybrid Inheritance.
# Requirements
# Create a class Person
# Attribute:
# name
# Method:
# display_person()
# Create a class Student that inherits from Person
# Attribute:
# student_id
# Method:
# display_student()
# Create a class SportsPlayer that inherits from Person
# Attribute:
# sport_name
# Method:
# display_sports_player()
# Create a class CollegeStudent that inherits from both Student and SportsPlayer
# Attribute:
# college_name
# Method:
# display_college_student()
# Create one object of CollegeStudent and display all details.


class Person():
    def __init__(self,name):
        self.name=name

    def display_person(self):
        print("name:",self.name)

class Student(Person):
    def __init__(self, name,student_id):
        self.student_id=student_id
        Person.__init__(self,name)

    def display_Student(self):
        print("student_id",self.student_id)

class SportsPlayer(Person):
    def __init__(self, name,sport_name):
        self.sport_name=sport_name
        Person.__init__(self,name)

    def display_sports_player(self):
        self.display_person()
        print("Sport name:", self.sport_name)

class CollegeStudent(Student, SportsPlayer):
    def __init__(self, name, student_id, sport_name,college_name):
        Student.__init__(self,name, student_id)
        SportsPlayer.__init__(self,name,sport_name)
        self.college_name=college_name

    def display_college_student(self):
        self.display_person()
        print("Student ID:",self.student_id)
        print("Sport Name:", self.sport_name)
        print("College name:",self.college_name)

obj=CollegeStudent("moulya","1GG22CS028","Kho-Kho","GECR")
obj.display_college_student()
        