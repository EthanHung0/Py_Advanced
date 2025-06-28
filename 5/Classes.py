from guizero import *

class Item:
    def __init__(self,id,title,author):
        self.id = id
        self.title = title
        self.author = author
    def get_info(self):
        return f"[ID: {self.id}] Title: {self.title} | Author: {self.author}"

class Book(Item):
    def __init__(self,id,title,author,pages):
        super().__init__(id,title,author)
        self.pages = pages
    def get_info(self):
        return f"[ID: {self.id}] Title: {self.title} | Author: {self.author} | Pages: {self.pages}"

class DVD(Item):
    def __init__(self,id,title,author,duration):
        super().__init__(id,title,author)
        self.duration = duration
    def get_info(self):
        return f"[ID: {self.id}] Title: {self.title} | Author: {self.author} | Duration: {self.duration}"

class Magazine(Item):
    def __init__(self,id,title,author,issue):
        super().__init__(id,title,author)
        self.issue = issue
    def get_info(self):
        return f"[ID: {self.id}] Title: {self.title} | Author: {self.author} | Issue: #{self.issue}"

#===================================================================================================

#Hierarchical inheritance
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"My name is {self.name}, im {self.age} years old. "

class Student(Person):
    def __init__(self, student_id, major, **kwargs):
        super().__init__(**kwargs)
        self.student_id = student_id
        self.major = major
    def introduce(self):
        return super().introduce() + f"ID {self.student_id}, I major in {self.major}"

class Teacher(Person):
    def __init__(self, teacher_id, subject, **kwargs):
        super().__init__(**kwargs)
        self.teacher_id = teacher_id
        self.subject = subject
    def introduce(self):
        return super().introduce() + f"ID {self.teacher_id}, I teach {self.subject}"

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, student_id, major, subject):
        super().__init__(
            name=name,
            age=age,
            student_id=student_id,
            major=major,
            teacher_id="TA123", #dummy
            subject=subject
        )
    def introduce(self):
        return f"My name is {self.name}, im {self.age} years old. ID {self.student_id}, I major in {self.major} and a teaching assistant for the course {self.subject}"


