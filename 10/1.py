
class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid Age: {age} (0 <= age <= 150)")

class Student:
    def __init__(self,name:str,age:int):
        self._name = name
        self.age = age

    @property
    def age(self):
        return self._age if hasattr(self,"_age") else None
    @age.setter
    def age(self,val):
        if val < 0 or val > 150:
            raise InvalidAgeError(val)
        self._age = val

# student_list = [Student("a",15),Student("b",16),Student("c",12),Student("d",-1),Student("e",200)]
Student("e",200)



