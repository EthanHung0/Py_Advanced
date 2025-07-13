from abc import ABC,abstractmethod

class CanBo(ABC):
    def __init__(self,name,address):
        self._name = name
        self._age = None
        self._gender = None
        self._address = address

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        try:
            age = int(age)
        except ValueError:
            return False
        if 0 > age > 100:
            print("Invalid age.")
            return False
        self._age = age

    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self,gender):
        gender = gender.lower()
        if gender not in ["nam","nữ","khác"]:
            print("Invalid gender.")
            return False
        self._gender = gender
    @abstractmethod
    def show_info(self):
        pass


class CongNhan(CanBo):
    def __init__(self, name, address):
        super().__init__(name, address)
        self._grade = None #bac

    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self,grade):
        try:
            grade = int(grade)
        except ValueError:
            return False
        if grade not in range(1,11):
            print("Invalid grade.")
            return False
        self._grade = grade

    def show_info(self):
        return f"Tên: {self._name} | Tuổi: {self._age} | Giới tính: {self._gender} | Địa chỉ: {self._address} | Bậc {self._grade}"


class KySu(CanBo):
    def __init__(self, name, address, industry):
        super().__init__(name, address)
        self._industry = industry #nganh dao tao

    def show_info(self):
        return f"Tên: {self._name} | Tuổi: {self._age} | Giới tính: {self._gender} | Địa chỉ: {self._address} | Ngành đào tạo: {self._industry}"


class NhanVien(CanBo):
    def __init__(self, name, address, position):
        super().__init__(name, address)
        self._position = position #cong viec

    def show_info(self):
        return f"Tên: {self._name} | Tuổi: {self._age} | Giới tính: {self._gender} | Địa chỉ: {self._address} | Công việc: {self._position}"
