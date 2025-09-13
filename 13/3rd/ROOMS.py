from ABSTRACT_ROOM import Room


class Standard(Room):
    def __init__(self, room_id:str, price:str):
        super().__init__(room_id, price)

    def show_info(self) -> str:
        return f"Room ID: R{self._room_id} | Price: ${self._price} | Status: {f'room' if self._status else 'Vacant'}"



class VIP(Room):
    def __init__(self, room_id:str, price:str, services:list):
        super().__init__(room_id, price)
        self._services = services

    def show_info(self) -> str:
        return f"Room ID: R{self._room_id} | Price: ${self._price} | Status: {f'room' if self._status else 'Vacant'} | Services: {", ".join(self._services) + "."}"



class ConferenceRoom(Room):
    def __init__(self, room_id:str, price:str, capacity:str):
        super().__init__(room_id, price)
        self.capacity = capacity

    @property
    def capacity(self):
        return self._capacity if hasattr(self,"_capacity") else None
    @capacity.setter
    def capacity(self,amount):
        try:
            amount = int(amount)
            self._capacity = amount
        except ValueError:
            raise ValueError("capacity must be an integer value.")

    def show_info(self):
        return f"Room ID: R{self._room_id} | Price: ${self._price} | Status: {f'room' if self._status else 'Vacant'} | Capacity: {self._capacity}"



