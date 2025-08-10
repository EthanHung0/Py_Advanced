from abc import ABC,abstractmethod

class Middle(ABC):
    def __init__(self,name:str):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def getName(self):
        return self._name

#=================================================================================================

class Driver(Middle):
    def __init__(self, name:str):
        super().__init__(name)

#=================================================================================================

class GrandPrix(Middle):
    def __init__(self, name:str):
        super().__init__(name)

#=================================================================================================

# class Time:
#     def __init__(self):
#         self.