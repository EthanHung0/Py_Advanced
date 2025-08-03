from student import Student
import time

class StudentManager(): #What this does: add, update, delete, and display student records using the imported Student class.
    def __init__(self):
        self._student = []

    @property
    def student(self):
        return self._student

#====================================================================================================================
    def add_student(self):
        new_name = input("Nhập tên học sinh mới: ")
        new_age = input("Nhập tuổi học sinh mới: ")
        new_grades = input("Nhập các điểm học sinh mới (số thực) (ngăn cách bằng dấu phấy ','): ")

        stripped_grades = None
        try:
            stripped_grades = [float(item.strip()) for item in new_grades.split(",")]
        except ValueError:
            print("\n|Lỗi khi thêm học sinh: Điểm không hợp lệ.")
            time.sleep(0.5)

        try:
            self.student.append(Student(new_name,new_age,stripped_grades))
            print("\n|Đã thêm học sinh mới.")
            time.sleep(0.5)
        except ValueError as e:
            print(f"\n|Lỗi khi thêm học sinh: {e}")
            time.sleep(0.5)

#====================================================================================================================
    def update_grades(self):
        if not self.student:
            print("\n|Danh sách học sinh rỗng.")
            time.sleep(0.5)
            return

        print("\n|Đang hiện danh sách...")
        time.sleep(0.5)
        print("---Danh sách các học sinh hiện có---")
        for i,s in enumerate(self.student,1):
            print(f"|{i}. {s.display_info()}")
        try:
            choice = int(input(f"Chọn học sinh muốn cập nhật (1 - {len(self.student)}): "))
        except ValueError:
            print("\n|Lỗi: Lựa chọn không hợp lệ.")
            time.sleep(0.5)
            return

        if choice not in range(1,len(self.student)+1):
            print("\n|Lỗi: Lựa chọn không hợp lệ.")
            time.sleep(0.5)
            return

        update_student = self.student[choice-1]
        new_grades = input("Nhập các điểm mới trong số thực (ngăn cách bằng dấu phấy ','): ")
        try:
            stripped_grades = [float(item.strip()) for item in new_grades.split(",")]
        except ValueError:
            print("\n|Lỗi khi cập nhật điểm: Điểm không hợp lệ.")
            time.sleep(0.5)
            return

        update_student.grades = stripped_grades
        print("\n|Điểm mới đã được cập nhật.")
        time.sleep(0.5)

#====================================================================================================================
    def delete_student(self):
        if not self.student:
            print("\n|Danh sách học sinh rỗng.")
            time.sleep(0.5)
            return

        print("\n|Đang hiện danh sách...")
        time.sleep(0.5)
        print("---Danh sách các học sinh hiện có---")
        for i,s in enumerate(self.student,1):
            print(f"|{i}. {s.display_info()}")
        try:
            choice = int(input(f"Chọn học sinh muốn xóa (1 - {len(self.student)}): "))
        except ValueError:
            print("\n|Lỗi: Lựa chọn không hợp lệ.")
            return

        if choice not in range(1,len(self.student)+1):
            print("\n|Lỗi: Lựa chon không hợp lệ.")
            return

        self.student.remove(self.student[choice-1])

#====================================================================================================================
    def show_all_students(self):
        if not self.student:
            print("\n|Danh sách học sinh rỗng.")
            time.sleep(0.5)
            return

        print("\n|Đang hiện danh sách...")
        time.sleep(0.5)
        print("---Danh sách các học sinh hiện có---")
        for i,s in enumerate(self.student,1):
            print(f"|{i}. {s.display_info()}")
        input(">")
