"""
Create 3 classes with interconnection between them (Student, Teacher,
Homework)
Use datetime module for working with date/time
1. Homework takes 2 attributes for __init__: tasks text and number of days to complete
Attributes:
    text - task text
    deadline - datetime.timedelta object with date until task should be completed
    created - datetime.datetime object when the task was created
Methods:
    is_active - check if task already closed
2. Student
Attributes:
    last_name
    first_name
Methods:
    do_homework - request Homework object and returns it,
    if Homework is expired, prints 'You are late' and returns None
3. Teacher
Attributes:
     last_name
     first_name
Methods:
    create_homework - request task text and number of days to complete, returns Homework object
    Note that this method doesn't need object itself
PEP8 comply strictly.
"""
import datetime

class Homework:
    def __init__(self, text, days_to_complete):
        self.text = text
        self.created = datetime.datetime.now()
        self.deadline = self.created + datetime.timedelta(days=days_to_complete)

    def is_active(self):
        return datetime.datetime.now() <= self.deadline


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def do_homework(self, homework):
       
        if homework.is_active():
            return homework
        else:
            print('You are late')
            return None


class Teacher:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text, days_to_complete):
        return Homework(text, days_to_complete)


if __name__ == '__main__':
    teacher = Teacher('Dmitry', 'Orlyakov') 
    student = Student('Vladislav', 'Popov')

    expired_homework = teacher.create_homework('Learn functions', 0)
    
    print(f"Created on: {expired_homework.created}")  
    print(f"Deadline: {expired_homework.deadline}")  
    print(f"Task: {expired_homework.text}")  

    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('Create 2 simple classes', 5)
    print(f"OOP Homework deadline: {oop_homework.deadline}")  

    student.do_homework(oop_homework)  
    student.do_homework(expired_homework)  
