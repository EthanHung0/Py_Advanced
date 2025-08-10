

class Beverage:
    def __init__(self,name:str,price:float):
        self._name = name
        # self.quantity = quantity
        self.price = price #usd

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,string):
        if not isinstance(string,str):
            raise ValueError("name it with a string, dumbass")

    # @property
    # def quantity(self):
    #     return self._quantity if hasattr(self,"_quantity") else None
    # @quantity.setter
    # def quantity(self,val):
    #     try:
    #         self._quantity = int(val)
    #     except ValueError:
    #         print("Invalid Quantity value.")

    @property
    def price(self):
        return self._price if hasattr(self,"_price") else None
    @price.setter
    def price(self,val):
        try:
            self._price = float(val)
        except ValueError:
            raise ValueError("Invalid Price value.")

#=================================================================================================
class CustomerCard:
    def __init__(self, card_id, credit):
        self._card_id = card_id
        self.credit = credit

    @property
    def card_id(self):
        return self._card_id

    @property
    def credit(self):
        return self._credit if hasattr(self,"_credit") else None
    @credit.setter
    def credit(self,val):
        if not isinstance(val,(float,int)):
            raise ValueError("Invalid credit value.")
        self._credit = float(val)


    def add_credit(self,val):
        if not isinstance(val,(float,int)):
            raise ValueError("Invalid credit value.")
        self._credit += float(val)

    def spend(self,val):
        if not isinstance(val,(float,int)):
            raise ValueError("Invalid credit value.")
        self._credit -= float(val)