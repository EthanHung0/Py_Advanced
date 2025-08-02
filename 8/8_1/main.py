from classes import Customer, Store


def main():
    konbini = Store()

    print(konbini.list_products())

    cus_name = input("Enter Customer's name: ")
    customer = Customer(cus_name)
    while True:
        item_name = input("\nInput what you want to buy: ")
        if konbini.find_product(item_name):
            customer.add_to_cart(konbini.find_product(item_name))
        else:
            continue
        stop = input("\nStop shopping? (Y to stop)\n> ").lower()
        if stop == "y":
            break

    customer.checkout()
    print()
    print("Thank you!")

main()

