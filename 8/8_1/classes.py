import time

class Product:
    def __init__(self,name,price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name
    @property
    def price(self):
        return self._price

    def get_info(self):
        return f"Name: {self.name} | Price: ${self.price}"


class Customer:
    def __init__(self,name):
        self.name = name
        self.cart = [] # list of products

    def add_to_cart(self,product):
        self.cart.append(product)

    def checkout(self):
        print("Calculating total cost...")
        total = 0
        for i in self.cart:
            total += i.price
        time.sleep(0.5)
        print("> Printing receipt...")
        time.sleep(0.5)
        print(f"---Receipt---")
        print(f"Customer: {self.name}")
        print("Cart:")
        for i in self.cart:
            print(f"- {i.name} ({i.price})")
        print(f"Total cost: ${total}")
        input("> ")



class Store:
    def __init__(self):
        self.stock = [Product("Apple",10.0),Product("Milk",15.5),Product("Bread",5.0)]

    def list_products(self):
        info = "\n=== コンビニ ===\n"
        for i,item in enumerate(self.stock,1):
            info += f"{i}. {item.name} - ${item.price}\n"
        return info

    def find_product(self,name):
        print(f'> Finding product named "{name}"...')
        time.sleep(0.5)
        for i in self.stock:
            if i.name == name:
                print(f"> Added {i.name} - ${i.price} to cart.")
                return i
        print('> Product "{name}" not found.')
        return False



