from Classes import Ca_Nhan
import re
import time

class HoGiaDinh:
    def __init__(self,house_num):
        self._house_num = house_num
        self._member_list = []

    @property
    def house_num(self):
        return self._house_num
    @house_num.setter
    def house_num(self,val):
        if not self._is_valid_house_number(val):
            return False
        self._house_num = val


    def add_member(self,nguoi:Ca_Nhan):
        self.member_list.append(nguoi)


    def _is_valid_house_number(self,house_num):
        return bool(re.fullmatch(r'[A-Za-z0-9/]+', house_num))


    def show_info(self):
        if not self._member_list:
            print("Không có người trong hộ này.")
            time.sleep(0.5)
            return
        for i,j in enumerate(self._member_list,1):
            print(f"Số nhà: {self._house_num}")
            print("Các thành viên:")
            print(f"{i}. {j}")
            if j == self._member_list[-1]:
                print(f"Số thành viên: {i}")


    def small_scale_find(self,cmnd):
        print(f"Đang tìm kiếm trong hộ {self._house_num}...")
        time.sleep(0.5)
        for i in self._member_list:
            if i.cmnd == cmnd:
                print("Đã tìm thấy người có cùng số CMND.")
                time.sleep(0.3)
                print(f"\n{i}\n")
                input("> ")
                return True