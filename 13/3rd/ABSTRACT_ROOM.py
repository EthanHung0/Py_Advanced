from abc import ABC,abstractmethod
from CUSTOMER import Customer


class RoomRegistry: #singleton
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.used_ids = set()
        return cls._instance


class Room(ABC):
    _used_room_ids = RoomRegistry()

    def __init__(self, room_id:str, price:str):
        self.room_id = room_id
        self.price = price
        self._status = False

    @property
    def room_id(self):
        return self._room_id if hasattr(self,"_room_id") else None
    @room_id.setter
    def room_id(self,r_id):
        if r_id in Room._used_room_ids.used_ids:
            raise ValueError("Cannot register an already existed Room ID.")
        if len(r_id) != 5:
            raise ValueError("Room IDs must be 5 letters and/or numbers.")
        self._room_id = r_id
        Customer._used_room_ids.used_ids.add(r_id)

    @property
    def status(self):
        return self._status

    @property
    def price(self):
        return self._price if hasattr(self,"_price") else None
    @price.setter
    def price(self,r_id):
        try:
            r_id = int(r_id)
            self._price = r_id
        except ValueError:
            raise ValueError("Room's price must be an integer value.")

    def update_status(self):
        self._status = not(self._status)

    @abstractmethod
    def show_info(self) -> str:
        pass
