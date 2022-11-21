from points import Point

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        if x2 < x1 or y2 < y1:
            raise ValueError

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

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


import unittest

class TestRectangle(unittest.TestCase):
    def test_ctor(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 0, -1, -1)
            Rectangle(0, 0, -1, 1)
            Rectangle(0, 0, 1, -1)

    def test_str(self):
        rect = Rectangle(1, 1, 2, 2)
        self.assertEqual(str(rect), f'[({rect.pt1.x}, {rect.pt1.y}), ({rect.pt2.x}, {rect.pt2.y})]')

    def test_repr(self):
        rect = Rectangle(1, 1, 2, 2)
        self.assertEqual(repr(rect), f'Rectangle({rect.pt1.x}, {rect.pt1.y}, {rect.pt2.x}, {rect.pt2.y})')

    def test_eq(self):
        rect = Rectangle(1, 1, 2, 2)
        rect1 = Rectangle(1, 1, 2, 2)
        self.assertEqual(rect, rect1)

        rect = Rectangle(0, 0, 1, 1)
        rect1 = Rectangle(1, 1, 2, 2)
        self.assertEqual(rect, rect1)

    def test_ne(self):
        rect = Rectangle(1, 1, 2, 3)
        rect1 = Rectangle(1, 1, 2, 2)
        self.assertNotEqual(rect, rect1)

        rect = Rectangle(0, 0, 1, 1)
        rect1 = Rectangle(1, 1, 2, 3)
        self.assertNotEqual(rect, rect1)

    def test_center(self):
        rect = Rectangle(0, 0, 1, 1)
        self.assertEqual(rect.center(), (0.5, 0.5))

        rect = Rectangle(-1, -1, 1, 1)
        self.assertEqual(rect.center(), (0, 0))

    def test_area(self):
        rect = Rectangle(0, 0, 1, 1)
        self.assertEqual(rect.area(), 1)
        self.assertEqual(rect.area(), 1.0)
        rect = Rectangle(-1, -1, 1, 1)
        self.assertEqual(rect.area(), 4)
        self.assertEqual(rect.area(), 4.0)

    def test_move(self):
        rect = Rectangle(0, 0, 1, 1)
        rect.move(1, 1)
        expected = Rectangle(1, 1, 2, 2)
        self.assertEqual(rect, expected)

        rect = Rectangle(-1, -1, 1, 1)
        rect.move(-1, -1)
        expected = Rectangle(-2, -2, 0, 0)
        self.assertEqual(rect, expected)

        rect = Rectangle(-1, -1, 1, 1)
        rect.move(-1, 1)
        expected = Rectangle(-2, 0, 0, 2)
        self.assertEqual(rect, expected)

if __name__ == '__main__':
    unittest.main()