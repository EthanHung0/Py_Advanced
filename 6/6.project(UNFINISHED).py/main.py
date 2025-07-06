from Payments.credit_card import CreditCard
from Payments.crypto_wallet import CryptoWallet
from Payments.paypal import PayPal
from Payments.TransactionSystem import TransactionSystem as TS

def main():
    system = TS()

    while True:
        print("""
------------------------------------
|      Payment Gateway System      |
------------------------------------""")
        print("1. Add a payment method.")
        print("2. Make a payment.")
        print("3. Check balances.")
        print("4. Exit.")
        choice = input("Your choice: ")

        if choice == '1':
            system.add_method()

        elif choice == '2':
            system.make_payment()
        elif choice == '3':
            system.check_bals()
        elif choice == '4':
            print("Shutting down.")
            break
        else:
            print("Invalid choice.")

main()

