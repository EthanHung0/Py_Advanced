

class Rectangle:
    def __init__(self):
        self._width = None
        self._height = None
        self._area = None

    def _cal_area(self):
        if self._width and self._height:
            self._area = self._width*self._height

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,val):
        if val > 0:
            self._width = val
            self._cal_area()
        else:
            print("Invalid.")

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,val):
        if val > 0:
            self._height = val
            self._cal_area()
        else:
            print("Invalid.")

    @property
    def area(self):
        if self._area:
            return self._area
        else:
            return "Missing element."

a = Rectangle()
a.width = 1
a.height = 15.2
print(a.area)