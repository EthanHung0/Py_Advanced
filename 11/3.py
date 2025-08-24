from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Square(Shape):
    def draw(self):
        print("Drew a Square.")

class Circle(Shape):
    def draw(self):
        print("Drew a Circle.")

class Triangle(Shape):
    def draw(self):
        print("Drew a triangle.")

class ShapeFactory:
    def create_shape(shape:str):
        if shape.lower() == "square":
            return Square()
        elif shape.lower() == "circle":
            return Circle()
        elif shape.lower() == "square":
            return Triangle()


