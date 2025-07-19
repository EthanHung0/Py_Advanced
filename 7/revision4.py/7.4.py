from KhuPho import KhuPho

def main():
    system = KhuPho()

    while True:
        print("""
------------------------------------
|   QUẢN LÝ HỘ DÂN TRONG KHU PHỐ   |
------------------------------------""")
        print("1. Nhập n hộ dân vào khu phố.")
        print("2. Hiển thị thông tin các hộ dân.")
        print("3. Tìm người theo số CMND.")
        print("4. Thoát.")
        choice = input("Lựa chọn: ")

        if choice == '1':
            system.household_inputsys()
        elif choice == '2':
            system.show_all_info()
        elif choice == '3':
            find = input("Nhập CMND của người cần tìm trong khu phố: ")
            if not find.isdigit():
                print("Số CMND không hợp lệ.")
                continue
            system.large_scale_find(find)
        elif choice == '4':
            print("Đang thoát...")
            break
        else:
            print("Lựa chọn không khả thi.")

main()