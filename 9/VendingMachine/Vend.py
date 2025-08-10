from BEVnCARD import Beverage,CustomerCard
from COLLUMN import Collumn


class VendingMachine:
    def __init__(self):
        self._collumns = [ #dont know what this does
            Collumn(0,Beverage("Lemon Dou (HoneyLemon)",1.3)), #name, quantity, price in usd
            Collumn(1,Beverage("Lemon Dou (SignatureLemon)",1.4)),
            Collumn(2,Beverage("Lemon Dou (PeachLemon)",1.5)),
            Collumn(3,Beverage("Lemon Dou (DevilLemon)",1.5)),
            Collumn(4),
            Collumn(5)
        ]

        self._cards = [
            CustomerCard("card1",500), #id, credit
            CustomerCard("card2",150)
        ]


    def _isfull(self):
        return all([col.item is not None for col in self._collumns]) #dont know what this does

    def _bev_list(self):
        return [col.item.name.lower() for col in self._collumns]

    def _find_card(self,card_id): #dont know what this does
        for card in self._cards:
            if card.card_id == card_id:
                return card
        print(F"Customer Card [ID:{card_id}] not found.")

#==================

    def addBeverage(self,collumn_id,beverage:Beverage,quantity): # collumn id from 0-5
        if self._isfull:
            print("Vending Machine is full.")
            return
        if not isinstance(beverage,Beverage):
            raise ValueError('"beverage" parameter must be a Beverage object.')
        if collumn_id not in [1,2,3,4,5]:
            raise ValueError('"collumn_id" paremeter must be an integer from 0-5.')
        col = self._collumns[collumn_id]
        if col.item is None:
            raise ValueError("You can't add a beverage where already has one.")
        if beverage.name in self._bev_list:
            print("This beverage already exists.")
            return
        self._collumns[collumn_id] = Collumn(collumn_id,quantity,beverage) # black magic, i know.

    def rechargeCard(self,card_id,credit):
        card = self._find_card(card_id)
        card.add_credit(credit)

    def getCredit(self,card_id):
        found = self._find_card(card_id)
        print(found.credit)

    def refillCollumn(self,collumn_id:int,bev_name:str,new_quantity:int):
        if collumn_id not in [1,2,3,4,5]: #repetetive shit, not like im gonna care
            raise ValueError('"collumn_id" paremeter must be an integer from 0-5.')
        if not isinstance(bev_name,str):
            raise ValueError("the name is a string, dumbass")
        if not isinstance(new_quantity,int):
            raise ValueError("Set the new quantity with an integer, man.")
        if self._collumns[collumn_id].item.name != bev_name:
            raise ValueError("Unmatched Collumn ID and Beverage name.")
        self._collumns[collumn_id].quantity = new_quantity # this is so messy

    def availableCans(self,bev_name):
        if not isinstance(bev_name,str):
            raise ValueError("the name is a string, dumbass")
        for col in self._collumns:
            if col.item.name.lower() == bev_name.lower():
                return col.quantity
        print(f'Beverage "{bev_name}" not found.')

    def sellBeverage(self,bev_name,card_id):
        if not isinstance(bev_name,str):
            raise ValueError("the name is a string, dumbass")
        card = self._find_card(card_id)
        found = False
        for col in self._collumns:
            if col.item.name.lower() == bev_name.lower(): #repetetive shit again
                col.sell()
                card.spend(col.item.price)
                print(f'Sold a "{col.item.name}" - ${col.item.price} to Card[ID:{card.card_id}]')
                found = True
        if not found:
            print(f'Beverage "{bev_name}" not found.')
            return

    def getBeveragePrice(self,bev_name):
        if not isinstance(bev_name,str):
            raise ValueError("the name is a string, dumbass")
        for col in self._collumns:
            if col.item.name.lower() == bev_name.lower():
                return col.item.price






























