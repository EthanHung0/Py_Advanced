from BEVnCARD import Beverage

class Collumn:
    def __init__(self,collumn_id,quantity=0,item:Beverage=None):
        self.collumn_id = collumn_id #0-5
        self.quantity = quantity
        self._item = item

    @property
    def collumn_id(self):
        return self._collumn_id if hasattr(self,"_collumn_id") else None
    @collumn_id.setter
    def collumn_id(self,c_id):
        try:
            c_id = []
            if int(c_id) not in [0,1,2,3,4,5]:
                raise ValueError("Collumn ID must be an integer from 0-5.")
            self._collumn_id = int(c_id)
        except ValueError:
            raise ValueError("Collumn ID must be an integer from 0-5.")

    @property
    def item(self):
        return self._item

    @property
    def quantity(self):
        return self._quantity if hasattr(self,"_quantity") else None
    @quantity.setter
    def quantity(self,val):
        try:
            self._quantity = int(val)
        except ValueError:
            raise ValueError("Quantity must be an integer.")

    def sell(self):
        self._quantity -= 1