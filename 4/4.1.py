import sys
class Student:
    def __init__(self):
        self._age = None
        self._name = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,val):
        if isinstance(val,int) and type(val) == int and 10<=val<=100:
            self._age = val
        else:
            print("Invalid age input.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,n):
        if isinstance(n,str):
            self._name = n
        else:
            print("Value Error.")

a = Student()
a.name = "Aaron"
a.age = 9