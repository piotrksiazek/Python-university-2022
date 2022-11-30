from points import Point

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        if x2 < x1 or y2 < y1:
            raise ValueError

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    @classmethod
    def from_points(cls, points):
        return Rectangle(points[0].x, points[0].y, points[1].x, points[1].y)

    @property
    def top(self):
        return self.pt2.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def right(self):
        return self.pt2.x

    @property
    def width(self):
        return self.pt2.x - self.pt1.x

    @property
    def height(self):
        return self.pt2.y - self.pt1.y
    
    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def bottomleft(self):
        return self.pt1
    
    @property
    def topright(self):
        return self.pt2
    
    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt1.y)

    def __str__(self):
        return f'[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]'

    def __repr__(self):
        return f'Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})'

    def __eq__(self, other):
        horizontal = self.pt1.x - self.pt2.x == other.pt1.x - other.pt2.x
        vertical = self.pt1.y - self.pt2.y == other.pt1.y - other.pt2.y

        return horizontal and vertical

    def __ne__(self, other): 
        return not self == other

    def center(self):
        x = (self.pt2.x + self.pt1.x)/2
        y = (self.pt2.y + self.pt1.y)/2

        return (x, y)

    def area(self):
        x = self.pt2.x - self.pt1.x
        y = self.pt2.y - self.pt1.y

        return x*y

    def move(self, x, y):
        self.pt1.x += x
        self.pt2.x += x
        self.pt1.y += y
        self.pt2.y += y

        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)