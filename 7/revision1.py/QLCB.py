from classes import CongNhan,KySu,NhanVien
import time
import pickle
import os

class QLCB:
    def __init__(self):
        self.CB_List = []


    def add_CB(self):
        CB_type = input("Loại cán bộ (Công nhân/Kỹ sư/Nhân viên): ").lower()
        new_name = input("Nhập họ tên cán bộ: ")
        new_age = input("Nhập tuổi (không quá 100): ")
        new_gender = input("Nhập giới tính (Nam/Nữ/Khác): ")
        new_address = input("Nhập địa chỉ: ")

        if CB_type in ["cn","công nhân"]:
            new_grade = input("Công nhân bậc (1-10): ")
            newCB = CongNhan(new_name,new_address)
            newCB.grade = new_grade
        elif CB_type in ["ks","kỹ sư"]:
            new_industry = input("Ngành đào tạo: ")
            newCB = KySu(new_name,new_address,new_industry)
        elif CB_type in ["nv","nhân viên"]:
            new_position = input("Công việc: ")
            newCB = NhanVien(new_name,new_address,new_position)
        else:
            print("Loại cán bộ không hợp lệ.")
            return

        newCB.age = new_age
        newCB.gender = new_gender

        if all([newCB.age,newCB.gender]):
            if CB_type in ["cn","công nhân"]:
                if not newCB.grade:
                    print("Đăng ký cán bộ mới thất bại.")
                    return
            self.CB_List.append(newCB)
            self._SortByType()
            print("Đăng ký cán bộ mới thành công.")
        else:
            print("Đăng ký cán bộ mới thất bại.")


    def find_CB(self,findname):
        found = False
        for CB in self.CB_List:
            if findname.lower() in CB.name.lower():
                print(f"\n | {CB.show_info()} |")
                found = True
                input(">")
        if not found:
            print("Không tìm thấy cán bộ cùng tên.")
            time.sleep(0.5)

    # def _SortByType(self):
    #     def sort_key(cb):
    #         if isinstance(cb,CongNhan):
    #             return 0
    #         elif isinstance(cb,KySu):
    #             return 1
    #         elif isinstance(cb,NhanVien):
    #             return 2
    #     self.CB_List.sort(key=sort_key)

    def _SortByType(self):
        self.CB_List.sort(key=lambda cb: \
                            0 if isinstance(cb,CongNhan) \
                                else (1 if isinstance(cb,KySu) \
                                    else 2))


    def show_all(self):
        if not self.CB_List:
            print("Không có cán bộ trong danh sách.")
            time.sleep(0.5)
            return
        print("  Danh sách cán bộ")
        print("---------------------")
        for CB in self.CB_List:
            print(f"\n{CB.show_info()}")


    def remove_CB(self,findname):
        found = False
        for CB in self.CB_List:
            if CB.name.lower() == findname.lower():
                self.CB_List.remove(CB)
                found = True
                print("")
        if not found:
            print("Không tìm thấy cán bộ cùng tên.")


    def save(self,file_name):
        if not file_name.endswith(".dat"):
            file_name += ".dat"
        try:
            with open(file_name,mode="wb") as f:
                pickle.dump(self.CB_List,f)
        except Exception as e:
            print(f"Lỗi khi lưu file: {e}.")


    def load(self):
        files = [f for f in os.listdir() if f.endswith(".dat")]
        if not files:
            print("Thư mục rỗng.")
            time.sleep(0.5)
            return

        print("Các file có thể đọc: ")
        for i,f in enumerate(files,1):
            print(f"\n{i}. {f}")

        try:
            choice = int(input(f"Chọn file để load (1-{len(files)}): "))
            if not 1 <= choice <= len(files):
                print("Lựa chọn không phù hợp.")
                return
            file_name = files[choice-1]
        except ValueError:
            print("Vui lòng nhập số.")
            return

        try:
            with open(file_name,mode="rb") as a:
                self.CB_List = pickle.load(a)
            print(f"Đang tải danh sách từ {file_name}...")
            time.sleep(0.5)
            print(f"Đã load thành công danh sách cán bộ từ {file_name}")
        except Exception as e:
            print(f"Lỗi khi load file: {e}.")
            time.sleep(0.5)

