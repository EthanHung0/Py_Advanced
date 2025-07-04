from .payment_method import PaymentMethod

class CreditCard(PaymentMethod):
    def __init__(self, username):
        super().__init__(username)
        self._card_number = None
        self._cvv = None
        # self.__authentication = False

    @property
    def card_number(self):
        return self._card_number
    @card_number.setter
    def card_number(self,num):
        if not isinstance(num,str):
            # print("Card number input must be a string!")
            return False
        self._card_number = num
    @property
    def cvv(self):
        return self._cvv
    @cvv.setter
    def cvv(self,num):
        if not isinstance(num,str):
            # print("CVV input must be a string!")
            return False
        self._cvv = num

    def authenticate(self):
        try:
            int(self._card_number)
            int(self._cvv)
        except (ValueError,TypeError):
            print("Invalid Card number/CVV.")
            return False
        if not(len(self._card_number) == 16 and len(self._cvv) == 4):
            print("Invalid Card number/CVV.")
            return False
        return True

    def pay(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Invalid amount input.")
            return False
        if self._balance >= amount:
            self._balance -= amount
            return True
        return False

    # def pay(self, amount):
    #     if self.__authentication:
    #         if self._balance >= amount:
    #             self._balance -= amount
    #             print(f"Transaction complete. {amount}$ is deducted from user balance.")
    #         else:
    #             print("User balance is insufficient.")
    #     else:
    #         print("Card information unverified.")