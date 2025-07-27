from student_manager import StudentManager
import time

def main():
    main_sys = StudentManager()

    while True:
        print("""
----------------------------------------
|           QUẢN LÝ HỌC SINH           |
----------------------------------------""")
        print("|1. Thêm học sinh.                     |")
        print("|2. Cập nhật điểm.                     |")
        print("|3. Xóa học sinh.                      |")
        print("|4. Hiển thị danh sách học sinh.       |")
        print("|5. Thoát.                             |")
        print("----------------------------------------")

        choice = input("Chọn chức năng: ")
        if choice == "1":
            main_sys.add_student()
        elif choice == "2":
            main_sys.update_grades()
        elif choice == "3":
            main_sys.delete_student()
        elif choice == "4":
            main_sys.show_all_students()
        elif choice == "5":
            print("Tắt chương trình...")
            break
        else:
            print("Lựa chọn không hợp lệ.")
            time.sleep(0.5)

main()



