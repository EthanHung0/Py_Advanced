from abc import ABC,abstractmethod

class Ca_Nhan(ABC):
    _used_cmnds = set()

    def __init__(self,name,age,cmnd=None,job=None):
        self._name = name
        self._age = age
        self.cmnd = cmnd #gọi setter cmnd
        self._job = job

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return max(0,self._age)

    @property
    def cmnd(self):
        return self._cmnd if hasattr(self,"_cmnd") else None

    @cmnd.setter
    def cmnd(self, val):
        if not val:
            self._cmnd = None
            return
        try:
            int(val)
        except ValueError:
            raise ValueError("CMND không hợp lệ.")
        if val in Ca_Nhan._used_cmnds:
            raise ValueError(f"CMND '{val}' đã tồn tại.")
        self._cmnd = val #cho vào self._cmnd thay vì self.cmnd
        Ca_Nhan._used_cmnds.add(val)

    @property
    def job(self):
        return self._job

    @abstractmethod
    def __str__(self):
        pass
        # return f"Tên: {self.name} | Tuổi: {self.age} | Nghề nghiệp: {self.job} | CMND: {self.cmnd}"


class Younger(Ca_Nhan):
    def __init__(self,name,age,cmnd=None,job=None):
        super().__init__(name,age,cmnd,job)

    def __str__(self):
        if self.age < 14:
            return f"Tên: {self.name} | Tuổi: {self.age}"
        else:
            job_str = self.job if self.job else "Không có"
            cmnd_str = self.cmnd if self.cmnd else "Không có"
            return f"Tên: {self.name} | Tuổi: {self.age} | Nghề nghiệp: {job_str} | CMND: {cmnd_str}"


class Older(Ca_Nhan):
    def __init__(self, name, age, cmnd, job=None):
        super().__init__(name,age,cmnd,job)

    def __str__(self):
        job_str = self.job if self.job else "Không có"
        cmnd_str = self.cmnd
        return f"Tên: {self.name} | Tuổi: {self.age} | Nghề nghiệp: {job_str} | CMND: {cmnd_str}"



