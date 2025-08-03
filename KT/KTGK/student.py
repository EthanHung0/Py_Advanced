

class Student():
    def __init__(self, name:str, age:int, grades:list):
        self._name = name
        self.age = age
        self.grades = grades #list of float values
        self._avgrade = "N/A"
        self._performance = "N/A"

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age if hasattr(self,"_age") else None
    @age.setter
    def age(self,val):
        try:
            val = int(val)
            if val<0:
                raise ValueError("Tuổi không hợp lệ. (Không được âm)")
        except ValueError:
            raise ValueError("Tuổi không hợp lệ. (Nhập số nguyên)")
        self._age = val

    @property
    def grades(self):
        return self._grades
    @grades.setter
    def grades(self,vals):
        for i in vals:
            if i > 10:
                raise ValueError("Điểm không hợp lệ. (0-10)")
        self._grades = vals

    @property
    def avgrade(self):
        return self._avgrade

    @property
    def performance(self):
        return self._performance


    def calculate_average(self):
        total = sum(self.grades)
        self._avgrade = total/len(self.grades)
        return round(self._avgrade,2)


    def get_academic_performance(self):
        if self._avgrade == "N/A":
            self.calculate_average()

        if 0 <= self.avgrade < 5:
            self._performance = "Yếu"
        elif self._avgrade < 6.5:
            self._performance = "Trung Bình"
        elif self._avgrade < 8:
            self._performance = "Khá"
        elif self._avgrade <=10:
            self._performance = "Giỏi"
        return self.performance

    def display_info(self):
        return f"Tên: {self.name} | Tuổi: {self.age} | Điểm TB: {self.calculate_average()} | Học Lực: {self.get_academic_performance()}."


