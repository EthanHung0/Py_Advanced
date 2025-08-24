from abc import ABC,abstractmethod


class RoleError(Exception):
    def __init__(self):
        super().__init__()

class InvalidSSNError(Exception):
    def __init__(self):
        super().__init__("Invalid, SSN must be a 9 digits String.")

#-----------------------------------------------------------------------

class Patient_Role:
    pass

class Doctor_Role:
    def __init__(self, ID:str, speciality:str):
        self._ID = ID
        self._speciality = speciality
        self._assigned_patients = []

    @property
    def ID(self):
        return self._ID
    @property
    def speciality(self):
        return self._speciality

#-----------------------------------------------------------------------

class Person():
    _used_SSN = set()

    def __init__(self,first_name:str,surname:str,SSN:str,roles:set|None):
        self._first_name = first_name
        self._surname = surname
        self.SSN = SSN
        self._roles = roles if roles else set()

    @property
    def first_name(self):
        return self._first_name
    @property
    def surname(self):
        return self._surname
    @property
    def SSN(self):
        return self._SSN if hasattr(self, "_SSN") else None
    @SSN.setter
    def SSN(self,num):
        try:
            int(num)
            if len(num) != 9:
                raise InvalidSSNError
        except ValueError:
            raise InvalidSSNError
        self._SSN = num

    def assignRole(self,role:Patient_Role|Doctor_Role):
        if not isinstance(role,(Doctor_Role,Patient_Role)):
            raise RoleError(f'The role "{role}" does not exist.')
        self._roles.add(role)

    @property
    def roles(self):
        return self._roles if self._roles else None



















