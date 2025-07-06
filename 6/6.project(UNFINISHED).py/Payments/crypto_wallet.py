from .payment_method import PaymentMethod

class CryptoWallet(PaymentMethod):
    def __init__(self, username, balance):
        super().__init__(username, balance)
        self._private_key = None
        self._wallet_address = None
        # self.__authentication = False

    @property
    def wallet_address(self):
        return self._wallet_address
    @wallet_address.setter
    def wallet_address(self,address):
        if not isinstance(address,str):
            print("Wallet address input must be a string!")
            return
        if not(address.startswith("0x") and len(address) == 14):
            print("Invalid private key input. (must start with 0x and exactly 14 characters long)")
            return
        self._wallet_address = address
    @property
    def private_key(self):
        return self._private_key
    @private_key.setter
    def private_key(self,key):
        if not isinstance(key,str):
            print("Private key input must be a string!")
            return
        self._private_key = key

    def authenticate(self):
        authen = input("Enter Private key: ")
        if authen == self._private_key:
            return True
        print("Incorrect Private key.")
        return False

    def pay(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Invalid amount input.")
            return False
        if self._balance >= amount:
            self._balance -= amount
            return True
        return False

    def check_bal(self):
        return f"{self.balance} Coins"