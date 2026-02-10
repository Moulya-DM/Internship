# Problem: Student College System
# You want to create a student system where college name is same for all students.
# What to do
# Create class Student with:
# Class Variable
# college_name = "ABC College"
#  (common for all students)
# Constructor
# takes name and roll_no
# Classmethod
# change_college(new_name)
#  to update the college name for all students.
# Staticmethod
# is_pass(marks)
#  returns pass or fail (example: pass if marks >= 35)
# Instance method
# display() prints student details
# How it works
# Create 2 students
# Print both details
# Change college using classmethod
# Print again → both students should show new college name
# Use staticmethod to check pass/fail

class student:
    college_name = "ABC College"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    @classmethod
    def change_college(cls,new_name):
        cls.college_name=new_name

    def is_pass(marks):
        if marks>=35:
            print("Pass")
        else:
            print("fail")
    def display(self):
        print("The name of the student is",self.name)
        print("The roll number of the student is",self.roll_no)
    
s1=student("Abhi","123")
s2=student("balu","099")

s1.display()
s2.display()

print(student.college_name)
student.change_college("XYZ College")
print(s1.college_name)

student.is_pass(40)
student.is_pass(30)
