from guizero import *

class Item:
    def __init__(self,name,quantity,price,barcode):
        self.name = name
        if quantity < 0:
            quantity = 0
            info("Invalid Input","Invalid quantity input, quantity is set to 0.")
        self._quantity = quantity
        self.__price = price
        self.__barcode = barcode

    def __str__(self):
        return f"Item: Name = {self.name}, Quantity = {self._quantity}, Price = {self.__price} $, Barcode = {self.__barcode}"

    def get_amount(self):
        return self._quantity

    def get_price(self):
        return self.__price

    def update_price(self,new_price):
        if not new_price > 0:
            info("Error!","Invalid New Price.")
            return
        self.__price = new_price
        return True

    def update_barcode(self,new_barcode):
        if len(new_barcode) not in [8,12]:
            info("Error!","Invalid BarCode. (EAN-8 or UPC only)")
            return
        self.__barcode = new_barcode
        return True

    def check_storage(self):
            if self._quantity < 30:
                return "Running out of stock."
            elif self._quantity < 100:
                return "Stable stock."
            else:
                return "High stock."

    def get_barcode(self):
        return self.__barcode

    def Item_sell(self,amount):
        if amount > self._quantity:
            info("Unable to sell.","Not enough stock to sell.")
            return
        self._quantity -= amount
        return True

#---------------------------------------------------------------------

# items = [
#     Item("Fresh Milk Bottles", 12, 0.8, "001"),
#     Item("Instant Noodle Packets", 200, 0.2, "002"),
#     Item("Fragrant Rice Bags", 45, 0.7, "003"),
#     Item("Cooking Oil Bottles", 130, 1.15, "004")
# ]

# def Load_Items():
#     sorted_names = sorted(item.name for item in items) #sorts out alphabetically
#     for name in sorted_names:
#         ItemList.append(name)

# #---------------------------------------------------------------------

# management = App(title="Items Management.",width=400,height=500)

# def Item_Info():
#     list_selected = ItemList.value
#     if not list_selected:
#         info("No Selection.","Please select an item.")
#         return

#     selected_item = next((i for i in items if i.name == list_selected), None)
#     if selected_item is None:
#         info("Error.","Item Not Found.")
#         return

#     win = Window(management, title=selected_item.name, width=300, height=250)

#     name_text = Text(win, "", size=12)
#     quantity_text = Text(win, "", size=12)
#     price_text = Text(win, "", size=12)
#     barcode_text = Text(win, "", size=12)

#     def refresh():
#         name_text.value = f"Name: {selected_item.name}."
#         quantity_text.value = f"Quantity: {selected_item.get_amount()}. ({selected_item.check_storage()})"
#         price_text.value = f"Price: ${selected_item.get_price()}."
#         barcode_text.value = f"Barcode: {selected_item.get_barcode()}."

#     def sell_button():
#         q = question("Selling quantity", f"How many {selected_item.name} do you want to sell?")
#         if q == None:
#             return
#         if not q or not q.isdigit():
#             info("Error!", "Selling quantity must contain digits only.")
#             return
#         if selected_item.Item_sell(int(q)):
#             info("Success!", "Items Successfully Sold.")
#             refresh()

#     def upd_price_button():
#         def isfloat(s):
#             try:
#                 float(s)
#                 return True
#             except ValueError:
#                 return False

#         q = question("Update Price", "Input New Price:")
#         if q == None:
#             return
#         if not q or not isfloat(q):
#             info("Error!", "Invalid Input")
#             return
#         if selected_item.update_price(float(q)):
#             info("Success!", "Item Price Successfully Updated.")
#             refresh()

#     def upd_barcode_button():
#         q = question("Update Barcode", "Input New Barcode:")
#         if q == None:
#             return
#         if not q or not q.isdigit():
#             info("Error!", "Barcode must contain digits only.")
#             return
#         if selected_item.update_barcode(q):
#             info("Success!", "Item Barcode Successfully Updated.")
#             refresh()

#     buttons = Box(win, layout="grid")
#     PushButton(buttons, text="Sell", command=sell_button, grid=[0, 0])
#     PushButton(buttons, text="Update Price", command=upd_price_button, grid=[1, 0])
#     PushButton(buttons, text="Update Barcode", command=upd_barcode_button, grid=[2, 0])

#     refresh()

# Text(management,"Available Items",size=20,color="#264F10",bold=1)
# ItemList = ListBox(management,width=200,height=300)
# PushButton(management,text="Show Info",command=Item_Info)


# Load_Items()
# management.display()
