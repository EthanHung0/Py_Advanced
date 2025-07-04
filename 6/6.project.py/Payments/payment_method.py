from abc import ABC,abstractmethod

class PaymentMethod(ABC):
    def __init__(self,name:str):
        self.username = name
        self._balance = None
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self,val):
        if not isinstance(val,(int,float)):
            raise TypeError("Balance must be a number.")
        if val < 0:
            print("Balance input must be greater or equals to 0.")
            raise TypeError("Balance must be a number.")
        self._balance = val
    @abstractmethod
    def authenticate(self):
        pass
    @abstractmethod
    def pay(self,amount):
        pass

    def check_bal(self):
        return f"{self.balance}$"