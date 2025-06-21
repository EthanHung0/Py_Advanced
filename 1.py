#=========================================================================================
##BAI1:
# class SinhVien:

#     def __init__(self,ten,ma_so,lop,diem_tb):
#         self.ten = ten
#         self.ma_so = ma_so
#         self.lop = lop
#         self.diem_tb = diem_tb
#         if self.diem_tb>10 or self.diem_tb<0:
#             print("Điểm trung bình không hợp lệ.")

#     def in_thong_tin(self):
#         print(f"""
# Tên: {self.ten}
# Mã số sinh viên: {self.ma_so}
# Lớp: {self.lop}
# Điểm trung bình: {self.diem_tb}
# """)

#     def xep_loai(self):
#         if 0<=self.diem_tb<5:
#             ranking = "Yếu"
#         elif self.diem_tb<6.5:
#             ranking = "TB"
#         elif self.diem_tb<8:
#             ranking = "Khá"
#         else:
#             ranking = "Giỏi"
#         print(f"Học sinh {ranking}")

#     def cap_nhat_diem(self,new):
#         if new>10 or new<0:
#             print("Điểm trung bình mới không hợp lệ.")
#         else:
#             self.diem_tb = new
#             print("\n\n-Điểm đã được thay đổi")

# sv1 = SinhVien("Minh Hùng","001","A1",5.5)
# sv2 = SinhVien("Thanh Long","002","A2",8.4)
# sv3 = SinhVien("Tiến Anh","003","A3",7.6)

# def there():
#     for i in [sv1,sv2,sv3]:
#         print("==============================")
#         i.in_thong_tin()
#         i.xep_loai()
# there()

# sv1.cap_nhat_diem(8)
# there()


#=========================================================================================

import sys
class Car:
    def __init__(self,brand,year,color,car_type):
        self.brand = brand
        self.year = year
        self.color = color
        self.car_type = car_type.lower()
        if self.car_type == "electric":
            self.battery_level = 100 # (%)
        elif self.car_type == "gasoline":
            self.fuel_level = 50 # (liter)
        else:
            print("Invalid car type.")
            sys.exit()
    mileage = 0
    engine_on = False

    def start_engine(self):
        self.engine_on = True
        print(f"The car engine is turned on.")
    def stop_engine(self):
        self.engine_on = False
        print(f"The car engine is turned off.")

    counter = 0
    def drive(self,km):
        if not self.engine_on:
            print("Nothing happened. (Car engine is off)")
            return
        if type(km) != int:
            print("Invalid distance input (Integer value only)")

        distance = 0

        if self.car_type == "electric":
            while distance < km and self.battery_level > 10:
                self.battery_level -= 1
                distance += 1
            if distance < km:
                print(f"The car drove for {distance}km before stopping due to insufficient battery level. (Battery Level: 10%)")
            else:
                print(f"The car drove through {km}km. (Battery Level: {self.battery_level}%)")

        elif self.car_type == "gasoline":
            while distance < km and self.fuel_level > 5:
                distance += 1
                self.counter += 1
                if self.counter == 15:
                    self.fuel_level -= 1
                    self.counter = 0
            if distance < km:
                print(f"The car drove for {distance}km before stopping due to insufficient fuel. (Fuel: 5 liter)")
            else:
                print(f"The car drove through {km}km. (Fuel: {self.fuel_level} liter)")

        self.mileage += distance

    def car_info(self):
        print(f"""=============================
Brand: {self.brand}
Year: {self.year}
Color: {self.color}
Car Type: {self.car_type}
Mileage: {self.mileage} km""")
        if self.engine_on:
            print("Engine status: On.")
        else:
            print("Engine status: Off.")
        if self.car_type.lower() == "electric":
            print(f"Battery level: {self.battery_level}%.")
        else:
            print(f"Fuel: {self.fuel_level} liter.")
        print("=============================")

    def charge(self):
        if self.car_type != "electric":
            print("This is a gasoline car.")
            return
        self.battery_level = 100
        print("Charged car battery. (Battery Level: 100%)")
    def refill(self,amount):
        if self.car_type != "gasoline":
            print("This is an electric car.")
            return
        self.fuel_level += amount
        print(f"Refilled car fuel. (Fuel: {self.fuel_level} liter.)")

    def paint(self,color):
        self.color = color
        print(f"The car's color is now {self.color}")


car1 = Car("Mustang","1980","blue","gasoline")
car1.car_info()
car1.start_engine()
car1.drive(10)
car1.drive(5)
car1.refill(4)
car1.paint("red")
car1.car_info()