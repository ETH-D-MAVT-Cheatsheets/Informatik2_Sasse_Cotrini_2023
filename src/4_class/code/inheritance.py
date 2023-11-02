class Parent:
    def __init__(self, x1):
        self.x = x1
    def double_x(self):
        self.x *= 2

class Child(Parent):
    def __init__(self, x1, y1):
        Parent.__init__(self, x1)
        self.y = y1
    def double_y(self):
        self.y *= 2

c = Child(2, 2)
c.double_x()
print(c.x, c.y) #Output: 4 2