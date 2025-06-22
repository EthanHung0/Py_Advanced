class User:
    def __init__(self):
        self._first_name = None
        self._last_name = None
        self._email = None

    def _upd_email(self):
        if self._first_name and self._last_name:
            self._email = f"{self._first_name}.{self._last_name}@gmail.com"
        else:
            self._email = None

    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self,n):
        self._first_name = n
        self._upd_email()

    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self,n):
        self._last_name = n
        self._upd_email

    @property
    def email(self):
        self._email = f"{self._first_name}.{self._last_name}@gmail.com"
        return self._email
    @email.setter
    def email(self,value):
        self._first_name,self._last_name = value
        self._upd_email()


a = User()
a.first_name = "Ethan"
a.last_name = "Aaron"
print(a.email)
a.email = "Aaron","Ethan"
print(a.email)
print(a.first_name)
print(a.last_name)
