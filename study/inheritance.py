class Shape:
    def area(self):
        print('This is the area of your shape:')

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        super().area()
        print(self.side ** 2)

new_square = Square(7)
new_square.area()
