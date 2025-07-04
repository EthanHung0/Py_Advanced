import time

class TransactionSystem:
    def __init__(self):
        self._methods = []

    def add_method(self,method):
        self._methods.append(method)

    def _show_methods(self):
        print("Choose a payment method: ")
        for idx,method in enumerate(self._methods,1):
            desc = type(method).__name__
            if hasattr(method,"card_number"):
                desc += f" - Card Number: ****{method.card_number[-4:]}"
            elif hasattr(method,"email"):
                desc += f" - Email: {method.email[0]}***@{method.email.split("@")[-1]}"
            elif hasattr(method,"wallet_address"):
                desc += f" - Wallet: ...{method.wallet_address[-4:]}"
            print(f"{idx}. {desc}")

    def make_payment(self):
        if not self._methods:
            print("No methods available.")
            time.sleep(0.5)
            return
        self._show_methods()
        try:
            choice = int(input("> ")) - 1
            method = self._methods[choice]
        except (ValueError,TypeError,IndexError):
            print("Invalid choice.")
            return
        print("Entering authentication details...")
        time.sleep(0.5)
        if not method.authenticate():
            print("Authentication Failed.")
            return
        print("Authentication successful.")
        try:
            amount = float(input("Enter payment amount: "))
        except ValueError:
            print("Invalid amount input.")
            return
        print("Performing Transaction Progress..")
        time.sleep(0.5)
        if method.pay(amount):
            print("Transaction completed.")
            print(f"Remaining balance: {method.check_bal()}")
        else:
            print("Transaction failed.")

    def check_bals(self):
        if not self._methods:
            print("No methods available.")
            time.sleep(0.5)
            return
        for method in self._methods:
            print(f"{type(method).__name__} ({method.username}): {method.method.check_bal()}")
