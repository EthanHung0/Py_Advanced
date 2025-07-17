from HGD import HoGiaDinh
from Classes import Younger,Older
import time

class KhuPho:
    def __init__(self):
        self.household_list = []

    def _add_household(self,hh:HoGiaDinh):
        self.household_list.append(hh)

    def household_inputsys(self):
        try:
            amount = int(input("Nhập số lượng hộ gia đình muốn thêm: "))
        except ValueError:
            print("Lỗi, Vui lòng nhập số.")
            time.sleep(0.5)
            return
        for i in range(amount):
            print(f"\nNhập thông tin cho hộ dân thứ {i + 1}:")
            new_house_num = input("Số nhà: ")
            ho = HoGiaDinh(new_house_num)
            member_amount = int(input("Số thành viên: "))
            for j in range(member_amount):
                print(f"| Thành viên {j + 1}:")
                new_name = input("| Họ tên: ")
                try:
                    new_age = int(input("| Tuổi: "))
                except ValueError:
                    print("Lỗi, Tuổi không hợp lệ.")
                    pass
                if new_age < 24:
                    if new_age > 14:
                        new_job = input("| Nghề nghiệp (Nếu có): ") or None
                        new_cmnd = input("| Số CMND: ").strip() or None
                    ho.add_member(Younger(new_name,new_age,new_cmnd,new_job))
                else:
                    new_job = input("| Nghề nghiệp (Nếu có): ") or None
                    new_cmnd = input("| Số CMND: ")
                    ho.add_member(Older(new_name,new_age,new_cmnd,new_job))
            self._add_household(ho)

    def show_all_info(self):
        print("Đang hiển thị các hộ trong khu...")
        time.sleep(0.5)
        for i in self.household_list:
            print("")
            i.show_info()
        input("> ")

    def large_scale_find(self,find_cmnd):
        print("")
        found = False
        for i in self.household_list:
            if i.small_scale_find(find_cmnd):
                found = True
        if found == False:
            print("Không tìm thầy người có cùng số CMND.")
        input("> ")