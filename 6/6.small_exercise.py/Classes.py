from abc import ABC, abstractmethod
import math

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def run(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Started car engine."
    def run(self):
        return "The car is running."

class Bike(Vehicle):
    def start_engine(self):
        return "Started bike engine."
    def run(self):
        return "The bike is running."

class Boat(Vehicle):
    def start_engine(self):
        return "Started boat engine."
    def run(self):
        return "The boat is running."


#==================================================================================================

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

#Circle, Rectangle, Square, Triangle
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return round(math.pi*self.radius**2,2)
    def perimeter(self):
        return round(2*math.pi*self.radius,2)

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return round(self.width*self.height,2)
    def perimeter(self):
        return round((self.width+self.height)/2,2)

class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return round(self.side**2,2)
    def perimeter(self):
        return round(4*self.side,2)

class Triangle(Shape):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.half_perimeter = (self.x+self.y+self.z)/2
    def area(self):
        return round(math.sqrt(self.half_perimeter*(self.half_perimeter-self.x)*(self.half_perimeter-self.y)*(self.half_perimeter-self.z)),2)
    def perimeter(self):
        return round(self.half_perimeter*2,2)


#==================================================================================================

class PaymentMethod(ABC):
    def authenticate(self):
        pass
    def pay(self,amount):
        pass

# CreditCard, PayPal, CryptoWallet
class CreditCard(PaymentMethod):
    def __init__(self):
        self.access = False
    def authenticate(self):
        self.access = True
        print("Credit card Access Authenticated.")
    def pay(self,amount):
        if self.access == True:
            return f"{amount}$ has been paid with Credit card."
        else:
            return "Credit card Access Unauthenticated"

class PayPal(PaymentMethod):
    def __init__(self):
        self.access = False
    def authenticate(self):
        self.access = True
        print("PayPal Access Authenticated.")
    def pay(self,amount):
        if self.access == True:
            return f"{amount}$ has been paid with PayPal."
        else:
            return "PayPal Access Unauthenticated"

class CryptoWallet(PaymentMethod):
    def __init__(self):
        self.access = False
    def authenticate(self):
        self.access = True
        print("CryptoWallet Access Authenticated.")
    def pay(self,amount):
        if self.access == True:
            return f"{amount}$ has been paid with CryptoWallet."
        else:
            return "CryptoWallet Access Unauthenticated"


#==================================================================================================

class Employee(ABC):
    def __init__(self, name, id):
        self.name = name
        self.id = id
    @abstractmethod
    def calculate_salary():
        pass

# FullTimeEmployee, PartTimeEmployee, Freelancer
class FullTimeEmployee(Employee):
    def __init__(self, name, id):
        super().__init__(name, id)
    def calculate_salary(self,months):
        return f"{self.name}(ID{self.id}) Salary: {months*5000}$/{months}(month) (5000$/month)"

class PartTimeEmployee(Employee):
    def __init__(self, name, id):
        super().__init__(name, id)
    def calculate_salary(self,hours):
        return f"{self.name}(ID{self.id}) Salary: {hours*25}$/{hours}(hour) (25$/hour)"

class Freelancer(Employee):
    def __init__(self, name, id):
        super().__init__(name, id)
    def calculate_salary(self,projects):
        return f"{self.name}(ID{self.id}) Salary: {projects*3000}$/{projects}(project) (3000$/project)"


#==================================================================================================

class MediaPlayer(ABC):
    def __init__(self,filename):
        self.filename = filename

    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def pause(self):
        pass
    @abstractmethod
    def stop(self):
        pass

#MP3Player, VideoPlayer, StreamingPlayer.
class MP3Player(MediaPlayer):
    def __init__(self, filename):
        super().__init__(filename)
    def play(self):
        return f"Playing audio file: {self.filename}..."
    def pause(self):
        return f"Pausing audio file {self.filename}..."
    def stop(self):
        return f"Stopping audio file {self.filename}..."

class VideoPlayer(MediaPlayer):
    def __init__(self, filename):
        super().__init__(filename)
    def play(self):
        return f"Playing video file: {self.filename}..."
    def pause(self):
        return f"Pausing video file {self.filename}..."
    def stop(self):
        return f"Stopping video file {self.filename}..."

class StreamingPlayer(MediaPlayer):
    def __init__(self, filename):
        super().__init__(filename)
    def play(self):
        return f"Streaming content from: {self.filename}..."
    def pause(self):
        return f"Paused stream from {self.filename}..."
    def stop(self):
        return f"Stopped streaming content from {self.filename}..."


#==================================================================================================



