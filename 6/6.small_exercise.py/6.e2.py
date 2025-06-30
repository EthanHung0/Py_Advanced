from Classes import Circle,Rectangle,Square,Triangle

tlist = [Circle(5),Rectangle(4,6),Square(3),Triangle(3,7,5)]
for i in tlist:
    print(f"""
Area: {i.area()}
Perimeter: {i.perimeter()}""")