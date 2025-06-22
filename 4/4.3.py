

class User:
    def __init__(self):
        self._first_name = None
        self._last_name = None
        self._email = None

    __temp_first_name = None
    __temp_last_name = None
    __email_format = "{firstname}.{lastname}"

    @property
    def first_name(self):
        if self.email != None:
            self._first_name = self.email[:len(self._first_name)-1]
        return self._first_name
    @first_name.setter
    def first_name(self,n):
        self._first_name = n

    @property
    def last_name(self):
        if self.email != None:
            self._last_name = self.email[-(len(self._last_name)+10):]
        return self._last_name
    @last_name.setter
    def last_name(self,n):
        self._last_name = n

    @property
    def email(self):
        self._email = f"{self._first_name}.{self._last_name}@gmail.com"
        return self._email
    # @email.setter
    # def email(self,first,last):


a = User()
a.first_name = "Ethan"
a.last_name = "Aaron"
print(a.email)
