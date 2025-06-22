class Item:
    def __init__(self,id,title,author):
        self.id = id
        self.title = title
        self.author = author
    def show_info(self):
        print(f"[ID: {self.id}] Title: {self.title} | Author: {self.author}")

class Book(Item):
    def __init__(self,id,title,author,pages):
        super().__init__(id,title,author)
        self.pages = pages
    def show_info(self):
        print(f"[ID: {self.id}] Title: {self.title} | Author: {self.author} | Pages: {self.pages}")

class DVD(Item):
    def __init__(self,id,title,author,duration):
        super().__init__(id,title,author)
        self.duration = duration
    def show_info(self):
        print(f"[ID: {self.id}] Title: {self.title} | Author: {self.author} | Duration: {self.duration}")

class Magazine(Item):
    def __init__(self,id,title,author,issue):
        super().__init__(id,title,author)
        self.issue = issue
    def show_info(self):
        print(f"[ID: {self.id}] Title: {self.title} | Author: {self.author} | Issue: #{self.issue}")

stuff = [
    Book("B001","AIUEO","SomeJPGuy",150),
    DVD("D002","SieuNhanGao","holysh",7200),
    Magazine("M003","ThangSau","nxbongod",12)
    ]
for i in stuff:
    i.show_info()