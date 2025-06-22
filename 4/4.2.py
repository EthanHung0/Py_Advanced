

class BankAccount:

    def __init__(self):
        self._balance = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,val):
        if (isinstance(val,float) or isinstance(val,int)) and val >= 0:
            self._balance = float(val)
        else:
            print("Invalid balance input.")

a = BankAccount()
a.balance = 11.0
print(a.balance)