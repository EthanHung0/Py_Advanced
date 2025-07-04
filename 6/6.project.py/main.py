from Payments.credit_card import CreditCard
from Payments.crypto_wallet import CryptoWallet
from Payments.paypal import PayPal
from Payments.TransactionSystem import TransactionSystem as TS

def main():
    sys = TS()

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
            add_username = input("Input Username: ")
            print("Choose a Payment method: ")
            print("1. Credit Card.")
            print("2. PayPal.")
            print("3. Crypto Wallet.")
            add_choice = input("> ")
            try:
                add_bal = float(input("Input balance: "))
            except (ValueError,TypeError):
                print("Invalid balance input.")
                return
            if add_choice == '1':
                add_cardnum = input("Input Card Number: ")
                add_cvv = input("Input Card's CVV: ")
                new_method = CreditCard(add_username)
                new_method.balance = add_bal
                new_method.card_number = add_cardnum
                new_method.cvv = add_cvv
                sys.add_method(new_method)
            elif add_choice == '2':
                add_email = input("Input Paypal Email: ")
                add_password = input("Input User Password: ")
                new_method = PayPal(add_username)
                new_method.balance = add_bal
                new_method.email = add_email
                new_method.password = add_password
                sys.add_method(new_method)
            elif add_choice == '3':
                add_walletaddress = input("Input Wallet Address: ")
                add_privatekey = input("Input Private Key")
                new_method = CryptoWallet(add_username)
                new_method.balance = add_bal
                new_method.wallet_address = add_walletaddress
                new_method.private_key = add_privatekey
                sys.add_method(new_method)
            else:
                print("Invalid choice.")

        elif choice == '2':
            sys.make_payment()
        elif choice == '3':
            sys.check_bals()
        elif choice == '4':
            print("Shutting down.")
            break
        else:
            print("Invalid choice.")

main()

