import sys

class MatHang:
    def __init__(self,ten,so_luong,gia,ma_vach):
        self.ten = ten
        if so_luong < 0:
            so_luong = 0
        self._so_luong = so_luong
        self.__gia = gia
        self.__ma_vach = ma_vach

    def __str__(self):
        return f"Mặt Hàng: Tên = {self.ten}, Số lượng = {self._so_luong}, Giá = {self.__gia} VND, Mã Vạch = {self.__ma_vach}"

    def get_name(self):
        print(f"Tên mặt hàng: {self.ten}")

    def get_amount(self):
        print(f"Số lượng hiện có: {self._so_luong}")

    def get_price(self):
        print(f"Giá bán: {self.__gia:,} VND")

    def update_price(self,new_price):
        if not new_price > 0:
            print("Giá không hợp lệ!")
            return
        self.__gia = new_price

    def update_barcode(self,new_barcode):
        if len(new_barcode) not in [8,12]:
            print("Mã vạch mới không hợp lệ. (chỉ nhận mã EAN-8 hoặc UPC)")
            return
        self.__ma_vach = new_barcode

    def check_storage(self):
            if self._so_luong < 30:
                print(f"Số lượng: {self._so_luong}. (Săp hết hàng.)")
            elif self._so_luong < 100:
                print(f"Số lượng: {self._so_luong}. (Ổn định)")
            else:
                print(f"Số lượng: {self._so_luong}. (Nhiều)")

    def get_barcode(self):
        print(f"Mã vạch sản phẩm: {self.__ma_vach}")

    def sell(self,amount):
        if amount > self._so_luong:
            print("Không đủ hàng để bán.")
            return
        self._so_luong -= amount
        print("Đã bán thành công.")


hang = MatHang("Milo",10,10000,"14512361")
# print(hang.__gia)
print(hang._MatHang__gia)
print(hang)
hang.get_name()
hang.get_barcode()
hang.get_amount()
hang.get_price()


