from abc import ABC,abstractmethod
# from __future__ import annotations

class Middle(ABC):
    def __init__(self,name:str):
        self._name = name

    @abstractmethod
    def getName(self) -> str:
        pass

#=================================================================================================

class Driver(Middle):
    def __init__(self, name:str):
        super().__init__(name)
        self._points = 0
        self._raced = []

    def getName(self) -> str:
        return self._name

    def getPoints(self):
        return self._points

    def addRace(self,race:"GrandPrix"):
        self._raced.append(race)
        # self._points += self._calPoint(race.getPosition)

    # def _calPoint(self,position):
    #     point_system = {1:25, 2:18, 3:15, 4:12, 5:10, 6:8, 7:6, 8:4, 9:2, 10:1}
    #     return point_system.get(position,0)

    def getRaced(self) -> list["GrandPrix"]:
        return self._raced

    def addPoints(self,pts):
        self._points += pts

#=================================================================================================

class GrandPrix(Middle):
    def __init__(self, name:str):
        super().__init__(name)
        self._times = []

    def getName(self) -> str:
        return self._name

    def addTime(self,t:"Time"):
        self._times.append(t)

    def getGPRanking(self) -> list[Driver]:
        sorted_times = sorted(self._times, key= lambda t: t.totalMilsec())
        return [t.driver for t in sorted_times] # returns list of drivers with descending time

    def getPosition(self,driver:Driver) -> int | None:
        ranking = self.getGPRanking()
        return ranking.index(driver) + 1 if driver in ranking else None

#=================================================================================================

class Time:
    def __init__(self, gp:GrandPrix, driver:Driver, hours:int, minutes:int, seconds:int, milliseconds:int):
        self._gp = gp
        self._driver = driver
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self._milliseconds = milliseconds

    @property
    def driver(self):
        return self._driver

    def toString(self) -> str:
        return f"{self._hours}:{self._minutes:02}:{self._seconds:02}.{self._milliseconds:003}"

    def totalMilsec(self) -> int: # convert all to milliseconds for comparison
        return self._hours*3600000 + self._minutes*60000 + self._seconds*1000 + self._milliseconds
