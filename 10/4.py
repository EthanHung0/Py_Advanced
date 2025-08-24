
class InvalidQuantityError(Exception):
    def __init__(self,quantity):
        super().__init__(f"Invalid Quantity Value: {quantity} (quantity must be higher than 0).")

class OutOfStockError(Exception):
    def __init__(self,name,requested,available):
        super().__init__(f'The Product "{name}" only have {available} item(s) left in stock, cannot give {requested} items.')


class Product:
    def __init__(self,name:str,stock:int):
        self._name = name
        self._stock = stock

    def reduce_stock(self,quantity:int):
        if quantity <= 0:
            raise InvalidQuantityError(quantity)
        if quantity > self._stock:
            raise OutOfStockError(self._name,quantity,self._stock)
        self._stock -= quantity

class Order: # works like a shopping cart
    def __init__(self):
        self.items = []

    def add_product(self,product:Product,quantity:int):
        product.reduce_stock(quantity)
        self.items.append((product,quantity))
