from abc import ABC,abstractmethod

        #Abstract class
class Equipment(ABC):
    def __init__(self, name:str, weight:float, effective_range:float, power:float):
        self._name = name
        self.weight = weight
        self.effective_range = effective_range
        self.power = power

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight if hasattr(self,"_weight") else None
    @weight.setter
    def weight(self,value):
        try:
            self._weight = float(value)
        except ValueError: raise ValueError("Weight value must be a <float> value.")

    @property
    def effective_range(self):
        return self._effective_range if hasattr(self,"_effective_range") else None
    @effective_range.setter
    def effective_range(self,value):
        try:
            self._effective_range = float(value)
        except ValueError: raise ValueError("Effective range value must be a <float> value.")

    @property
    def power(self):
        return self._power if hasattr(self,"_power") else None
    @power.setter
    def power(self,value):
        try:
            self._power = float(value)
        except ValueError: raise ValueError("Power value must be a <float> value.")

    @abstractmethod
    def use(self, amount:None):
        pass

    @abstractmethod
    def display_info(self) -> str:
        pass




#==================================================================================

class Gun(Equipment):
    def __init__(self, name:str, weight:float, effective_range:float, power:float, ammo:int):
        super().__init__(name, weight, effective_range, power)
        self.ammo = ammo

    @property
    def ammo(self):
        return self._ammo if hasattr(self,"_ammo") else None
    @ammo.setter
    def ammo(self,value):
        try:
            value = int(value)
            if value < 0:
                raise ValueError("Ammunition musn't be lower than 0.")
            self._ammo = value
        except ValueError: raise ValueError("Ammo must be an <int> value.")


    def use(self, amount:None):
        try:
            if self._ammo == 0:
                raise ValueError("Out of ammunition.")

            amount = int(amount)
            if amount <= 0:
                raise ValueError("Atleast one round must be fired.")

            # Mag dump if firing amount is higher than remaining ammos.
            remaining = self._ammo - amount
            if remaining < 0:
                amount = self._ammo
            self._ammo -= amount

            print(f"Fired {amount} rounds, {self._ammo} remaining." if self._ammo != 0 else f"Mag dumped ({amount} rounds fired). 0 rounds remaining.")
        except ValueError: raise ValueError("Firing rounds must be an <int> value")


    def display_info(self) -> str:
        return f"Name: {self._name} | Weight: {self._weight} | Effective Range: {self._effective_range} | Power: {self._power}\n Remaining ammos: {self._ammo}"

#-----------------------------------------------------------
class Tank(Equipment):
    def __init__(self, name:str, weight:float, effective_range:float, power:float, armor:str):
        super().__init__(name, weight, effective_range, power)
        self._armor = armor

    def use(self,amount:None):
        print("Up! Shots fired! On the way!")

    def display_info(self) -> str:
        return f"Name: {self._name} | Weight: {self._weight} | Effective Range: {self._effective_range} | Power: {self._power}\n Armor: {self._armor}"

#-----------------------------------------------------------

class Airstrike(Equipment):
    def __init__(self, name:str, weight:float, effective_range:float, power:float, payload:int):
        super().__init__(name, weight, effective_range, power)
        self.payload = payload

    @property
    def payload(self):
        return self._payload if hasattr(self,"_payload") else None
    @payload.setter
    def payload(self,value):
        try:
            value = int(value)
            if value < 0:
                raise ValueError("Payload musn't be lower than 0.")
            self._payload = value
        except ValueError: raise ValueError("Payload must be an <int> value.")


    def _missile_call(self,count) -> str:
        if count == 1: return "Single"
        elif count == 2: return "Pair"
        elif 3 <= count <= 4: return "Salvo"
        elif 5 <= count <= 6:return "Volley"
        elif 7 <= count <= 9: return "Barrage"
        else: return "Full Payload"

    def use(self, amount:None):
        if self._payload == 0:
            raise ValueError("Out of missiles.")
        try:
            amount = int(amount)
            if amount <= 0:
                raise ValueError("Atleast one missile must be fired.")

            remaining = self._payload - amount
            if remaining < 0:
                amount = self._payload

            self._payload -= amount
            print(f"Fired {self._missile_call(amount)} ({amount} missile{'s' if amount > 1 else ''}), {self._payload} remaining.")
        except ValueError: raise ValueError("Firing load must be an <int> value.")


    def display_info(self) -> str:
        return f"Name: {self._name} | Weight: {self._weight} | Effective Range: {self._effective_range} | Power: {self._power}\n Current payload: {self._payload}"