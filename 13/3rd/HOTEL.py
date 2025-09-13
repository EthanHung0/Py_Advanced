from ABSTRACT_ROOM import Room
from CUSTOMER import Customer


class Main_Hotel:
    def __init__(self):
        self._Rooms:list[Room] = []
        self._Customers:list[Customer] = []

    def findByID(self,roomf_id:str) -> Room:
        if not self._Rooms:
            print("No Available Rooms.")
            return
        found = False
        for room in self._Rooms:
            if room.room_id == roomf_id:
                found = True
                return room
        if found == False:
            raise ValueError("Room not found.")

    def addRoom(self,room:Room):
        self._Rooms.append(room)

    def checkIn(self, roomf_id:str, customer_id:str, name:str, phone_num:int):
        if not self._Rooms:
            print("No Available Rooms.")
            return
        room = self.findByID(roomf_id)
        if room.status:
            raise ValueError(f"Room ID <{room.room_id}> is already rented.")
        self._Customers.append(Customer(customer_id, name, phone_num, room))
        room.update_status()

    def showRooms(self):
        if not self._Rooms:
            print("No Available Rooms.")
            return
        print("\n|-------------------- Available Rooms --------------------|\n")
        for i,room in enumerate(self._Rooms,1):
            print(f"| {i}. {room.show_info()} |")
        print("\n|---------------------------------------------------------|\n")

    def checkOut(self, roomf_id:str):
        if not self._Customers:
            print("No rooms are rented yet.")
            return
        room = self.findByID(roomf_id)
        room.checkout()

    def showCustomers(self):
        if not self._Customers:
            print("No rooms are rented yet.")
            return
        print("|-------------------- Customers --------------------|")
        for i,customer in enumerate(self._Customers,1):
            print(f"| {i}. {customer.show_info()} |")
        print(f"|--------------------------------------------------|")
