from Classes import Driver,GrandPrix,Time
# from typing import List


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

    def getDrivers(self) -> list[Driver]: #returns a list of all drivers
        return [driver for driver in self._drivers]

    def getDriver(self,name:str) -> Driver | None: #returns a driver based on name
        if not isinstance(name,str):
            raise ValueError("Driver's name must be a string.")
        for driver in self._drivers:
            if driver.name.lower() == name.lower():
                return driver
        return None

#---------------------------------------------

    def defineGrandPrix(self,name:str):
        if not isinstance(name,str):
            raise ValueError("The Grand Prix's name must be a string.")
        self._GPs.append(Driver(name))

    def getGPs(self) -> list[GrandPrix]: #returns a list of all grand prix-es
        return [gp for gp in self._GPs]

    def getGrandPrix(self,name:str) -> GrandPrix | None: #returns a grand prix based on name
        if not isinstance(name,str):
            raise ValueError("The Grand Prix's name must be a string.")
        for gp in self._GPs:
            if gp.name.lower() == name.lower():
                return gp
        return None

#---------------------------------------------

    def setTime(self, gp: GrandPrix, driver: Driver, hours: int, minutes: int, seconds: int, milliseconds: int) -> Time:
        time = Time(gp, driver, hours, minutes, seconds, milliseconds)
        gp.add_time(time)
        self.times.append(time)
        return time #flexibility

#---------------------------------------------

    def awardPoints(self,race:GrandPrix):
        point_system = {1:25, 2:18, 3:15, 4:12, 5:10, 6:8, 7:6, 8:4, 9:2, 10:1}

        ranking = race.getGPRanking()
        for position, driver in enumerate(ranking,1):
            driver.addPoints(point_system.get(position,0))


    def getChampionshipRanking(self) -> list[Driver]:
        return sorted(self.drivers, key= lambda d: d.getPoints(), reverse= True)