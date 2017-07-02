class Rectangle:
    def __init__(self, w, l):
        self.w = w
        self.l = l

    @property
    def area(self):
        return (self.w * self.l)

    @property
    def perimeter(self):
        return (self.l *2 + self.w * 2)


rect = Rectangle(3,4)
print(rect.perimeter)