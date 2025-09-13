from ROOMS import Room


class CustomerRegistry:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.used_ids = set()
        return cls._instance


class Customer:
    _used_cus_id = CustomerRegistry()

    def __init__(self, customer_id:str, name:str, phone_num:int, room:Room):
        self.customer_id = customer_id
        self._name = name
        self.phone_num = phone_num
        self._room = room

    @property
    def room(self):
        return self._room

    @property
    def customer_id(self):
        return self._customer_id if hasattr(self,"_customer_id") else None
    @customer_id.setter
    def customer_id(self,cus_id):
        if cus_id in Customer._used_cus_id.used_ids:
            raise ValueError("Cannot register an already existed Customer ID.")
        self._customer_id = cus_id
        Customer._used_cus_id.used_ids.add(cus_id)

    @property
    def name(self):
        return self._name

    @property
    def phone_num(self):
        return self._phone_num if hasattr(self,"_phone_num") else None
    def phone_num(self,num):
        try:
            int(num)
            num = str(num)
            if not len(num) == 9:
                raise ValueError("Customer's phone number must be exactly 9 digits.")
            self._phone_num = num
        except ValueError:
            raise ValueError("Invalid phone number input.")

    def rent(self,room:Room):
        self._room = room

    def show_info(self) -> str:
        return f"Customer ID: {self.customer_id} | Customer's Name: {self._name} | Phone Number: {self._phone_num} | Room (ID): {self._room._room_id}"









