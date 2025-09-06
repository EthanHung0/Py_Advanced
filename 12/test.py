"""Viết class Car có thuộc tính brand, year, method display_info(). Tạo 2 object từ class này và gọi method.

Sự khác biệt giữa instance attribute và class attribute là gì? Cho ví dụ code.

Viết class Animal có method sound(). Tạo class Dog và Cat kế thừa từ Animal và override sound(). In ra tiếng kêu của từng con.

Dùng @staticmethod và @classmethod khác nhau thế nào? Khi nào thì nên dùng?

Viết class Person có thuộc tính name (private) và method get_name() để lấy tên. Thử gọi person.__name trực tiếp xem điều gì xảy ra.

Trong Python, __str__ và __repr__ khác nhau thế nào?

Giải thích sự khác biệt giữa inheritance và composition. Khi nào thì nên dùng composition thay vì inheritance?

Polymorphism trong Python hoạt động thế nào? Cho ví dụ ngoài kế thừa (gợi ý: duck typing).

Tạo class BankAccount có method deposit(), withdraw(), get_balance(). Thêm rule: số dư không được âm. Làm sao implement?

Có cần thiết tất cả bài toán đều dùng OOP không? Khi nào procedural (hàm bình thường) sẽ tốt hơn?"""



class Car:
    def __init__(self,brand:str,year:str):
        self.brand = brand
        self.year = year

    def display_info(self):
        return f"Brand: {self.brand} | Year: {self.year}"

car1 = Car("Gucci","2099")
car2 = Car("Deluxe","2077")
car1.display_info()
car2.display_info()

#================================================================

"""
Class attribute là thuộc tính mặc định của 1 class, được dùng chung cho mọi object được tạo từ class đó. Class attribute chỉ có 1 bản copy cho mọi object.
Instance attribute là thuộc tính riêng biệt cho từng object được tạo từ class đó. Instance attribute có thể có nhiều bản cho từng object được tạo.
"""

#VD:
class example:
    class_attr = "This is a class attribute." # every object created has this same value

    def __init__(self,parameter):
        self.instance_attr = parameter # varies base on parameter.

theobject = example("This is an instance attribute.")
print(theobject.class_attr)
print(theobject.instance_attr)

#================================================================

from abc import ABC,abstractmethod
class Animal(ABC):
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        print("Meow.")

class Dog(Animal):
    def sound(self):
        print("Woof.")

#================================================================

"""
Static method là method dành cho class thay vì dành cho object của class đó (Instance attribute), tham số đầu tiên vẫn là self. Thường được dùng để tạo những method tiện ích chung cho class.
Class method là method dành cho class và có thể truy cập trực tiếp vào data của class (Class attribute), tham số đầu tiên là cls. Thường dùng cho quản lý data của class hoặc cần quyền truy cập vào data của class.
"""

#================================================================

class Person:
    def __init__(self,name):
        self.__name = name # protected

    def get_name(self):
        return self.__name

person = Person()
person.get_name()
# person.__name

#================================================================

"""
__str__ trình bày ra output mà con người có thể đọc được (human-readable), dành cho những tác vụ cho người dùng.
__repr__ cho ra output là 1 giá trị không rõ ràng và có khả năng tái tạo lại 1 object bằng giá trị đó (không nhất thiết), thường được dùng cho người lập trình trong debugging,...
"""

#================================================================

"""
Inheritance là mỗi quan hệ "is-a" giữa class thừa kế và class ban đầu (superclass)
Composition là mối quan hệ "has-a" giữa class và object của 1 class khác, class này lấy object class kia để giá trị riêng.
"""

#================================================================

"""
Polymorphism tức một phương thức/Class có thể có nhiều cách thức/hình/loại triển khai/object khác nhau
"""

#================================================================

class BankAccount:
    def __init__(self):
        self.balance = 0

    @property
    def balance(self):
        return self._balance if hasattr(self,"_balance") else None
    @balance.setter
    def balance(self,val):
        try:
            val = float(val)
            if val < 0:
                raise ValueError("Balance cant be negative (for some reason).")
            self._balance = val
        except ValueError:
            raise ValueError("Balance must be a float type value.")

    def balance(self,val):
        self._balance += val



#================================================================




#================================================================






