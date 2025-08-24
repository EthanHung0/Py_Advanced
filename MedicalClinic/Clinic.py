from Classes import *


class NoSuchPatientError(Exception):
    def __init__(self, SSN):
        super().__init__(f"Patient SSN: <{SSN[:3]}-{SSN[3:5]}-{SSN[5:]}> Not Found.")

class NoSuchDoctorError(Exception):
    def __init__(self, ID):
        super().__init__(f"Doctor ID: {ID} Not Found.")


class Clinic:
    def __init__(self):
        self.people = {} #ID/SSN : Person

    def addPatient(self,first_name:str,surname:str,SSN:str) -> Person:
        person = self.people[SSN]
        if not person:
            self.people.append(Person(first_name,surname,SSN,{Patient_Role}))
            return
        if person.first_name == first_name and person.surname == surname:
            self.people[SSN].assignRole(Patient_Role)


















