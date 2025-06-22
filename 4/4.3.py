class User:
    def __init__(self):
        self._first_name = None
        self._last_name = None
        self._email = None

    @property
    def first_name(self):
        if self._email != None:
            self._first_name = self._email[:len(self._first_name)]
        return self._first_name
    @first_name.setter
    def first_name(self,n):
        self._first_name = n

    @property
    def last_name(self):
        if self._email != None:
            self._last_name = self._email[-(len(self._last_name)+10):-10]
        return self._last_name
    @last_name.setter
    def last_name(self,n):
        self._last_name = n

    @property
    def email(self):
        if self._email != None:
            self._first_name = self._email[:len(self._first_name)]
        elif self._email != None:
            self._last_name = self._email[-(len(self._last_name)+10):-10]
        self._email = f"{self._first_name}.{self._last_name}@gmail.com"
        return self._email
    @email.setter
    def email(self,value):
        first,last = value
        self._email = f"{first}.{last}@gmail.com"


a = User()
a.first_name = "Ethan"
a.last_name = "Aaron"
print(a.email)
a.email = "Aaron","Ethan"
print(a.email)
print(a.first_name)
print(a.last_name)
