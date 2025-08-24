
class InvalidDimensionError(Exception):
    def __init__(self, val):
        super().__init__(f"Invalid Value: {val} (Can't be lower than 0)")


class Rectangle:
    def __init__(self,width:float,height:float):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width if hasattr(self,"_width") else None
    @width.setter
    def width(self,val):
        if val < 0:
            raise InvalidDimensionError(val)
        self._width = val

    @property
    def height(self):
        return self._height if hasattr(self,"_height") else None
    @height.setter
    def height(self,val):
        if val < 0:
            raise InvalidDimensionError(val)
        self._height = val


    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height)*2




