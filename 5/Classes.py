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