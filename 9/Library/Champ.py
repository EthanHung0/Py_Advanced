from Classes import Driver,GrandPrix


class Championship:
    def __init__(self):
        self._drivers = [] #driver list
        self._GPs = [] #grand prix list

    @property
    def drivers(self):
        return self._drivers
    @property
    def GPs(self):
        return self._GPs

#=============================================

    def createDriver(self,name:str):
        if not isinstance(name,str):
            raise ValueError("Driver's name must be a string.")
        self._drivers.append(Driver(name))

    def getDrivers(self): #returns a list of all drivers
        return [driver for driver in self._drivers]

    def getDriver(self,name:str): #returns a driver based on name
        if not isinstance(name,str):
            raise ValueError("Driver's name must be a string.")
        for driver in self._drivers:
            if driver.name.lower() == name.lower():
                return driver
        print(f'Driver "{name} not found."')

#---------------------------------------------

    def defineGrandPrix(self,name:str):
        if not isinstance(name,str):
            raise ValueError("The Grand Prix's name must be a string.")
        self._GPs.append(Driver(name))

    def getGPs(self): #returns a list of all grand prixes
        return [gp for gp in self._GPs]

    def getGrandPrix(self,name:str): #returns a grand prix based on name
        if not isinstance(name,str):
            raise ValueError("The Grand Prix's name must be a string.")
        for gp in self._GPs:
            if gp.name.lower() == name.lower():
                return gp
        print(f'Grand Prix "{name} not found."')