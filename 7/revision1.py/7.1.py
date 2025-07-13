from QLCB import QLCB
import time

def main():
    system = QLCB()

    while True:
        print("""
------------------------------------
|          QUẢN LÝ CÁN BỘ          |
------------------------------------""")
        print("1. Thêm cán bộ.")
        print("2. Xóa cán bộ (theo tên).")
        print("3. Hiển thị danh sách cán bộ.")
        print("4. Tìm kiếm cán bộ (theo tên).")
        print("5. Lưu danh sách qua file.")
        print("6. Load danh sách trong file.")
        print("7. Thoát.")
        choice = input("Your choice: ")

        if choice == '1':
            system.add_CB()
        elif choice == '2':
            remove_name = input("Nhập tên cần tìm: ")
            system.remove_CB(remove_name)
        elif choice == '3':
            system.show_all()
        elif choice == "4":
            find_name = input("Nhập tên cần tìm: ")
            system.find_CB(find_name)
        elif choice == "5":
            save_name = input("Nhập tên file lưu danh sách cán bộ: ")
            system.save(save_name)
        elif choice == "6":
            system.load()
        elif choice == '7':
            print("Đang tắt hệ thống...")
            time.sleep(0.5)
            break
        else:
            print("Invalid choice.")

main()


