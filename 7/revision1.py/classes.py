from abc import ABC,abstractmethod

class CanBo(ABC):
    def __init__(self,name,address):
        self._name = name
        self._age = None
        self._gender = None
        self._address = address

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        try:
            age = int(age)
        except ValueError:
            return False
        if age <= 0 or age > 100:
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
        info = f"Tên: {self._name}"
        if self._age is not None:
            info += f" | Tuổi: {self._age}"
        if self._gender:
            info += f" | Giới tính: {self._gender.title()}"
        if self._address:
            info += f" | Địa chỉ: {self._address}"
        if self._grade is not None:
            info += f" | Bậc: {self._grade}"
        return info


class KySu(CanBo):
    def __init__(self, name, address, industry):
        super().__init__(name, address)
        self._industry = industry #nganh dao tao

    def show_info(self):
        info = f"Tên: {self._name}"
        if self._age is not None:
            info += f" | Tuổi: {self._age}"
        if self._gender:
            info += f" | Giới tính: {self._gender.title()}"
        if self._address:
            info += f" | Địa chỉ: {self._address}"
        if self._industry:
            info += f" | Ngành đào tạo: {self._industry}"
        return info


class NhanVien(CanBo):
    def __init__(self, name, address, position):
        super().__init__(name, address)
        self._position = position #cong viec

    def show_info(self):
        info = f"Tên: {self._name}"
        if self._age:
            info += f" | Tuổi: {self._age}"
        if self._gender:
            info += f" | Giới tính: {self._gender.title()}"
        if self._address:
            info += f" | Địa chỉ: {self._address}"
        if self._position:
            info += f" | Công việc: {self._position}"
        return info
