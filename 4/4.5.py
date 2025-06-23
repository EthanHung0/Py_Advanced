

class Temperature:
    def __init__(self):
        self._celcius = None
        self._fahrenheit = None

    def _F_upd(self):
        if self._celcius:
            self._fahrenheit = round(self._celcius*1.8+32,2)
    def _C_upd(self):
        if self._fahrenheit:
            self._celcius = round((self._fahrenheit-32)/1.8,2)

    @property
    def celcius(self):
        return round(self._celcius,2)
    @celcius.setter
    def celcius(self,val):
        self._celcius = round(val,2)
        self._F_upd()

    @property
    def fahrenheit(self):
        return round(self._fahrenheit,2)
    @fahrenheit.setter
    def fahrenheit(self,val):
        self._fahrenheit = round(val,2)
        self._C_upd()

a = Temperature()
a.celcius = 15
print(a.fahrenheit)
a.fahrenheit = 68
print(a.celcius)