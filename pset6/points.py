import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def cross(self, other):
        return self.x * other.y - self.y * other.x
 
    def length(self):
        a = abs(self.x)
        b = abs(self.y)

        return math.sqrt(a**2 + b**2)

    def __hash__(self):
        return hash((self.x, self.y))

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Point(1,2)), "(1, 2)")

    def test_repr(self):
        self.assertEqual(repr(Point(1,2)), "Point(1, 2)")

    def test_eq(self):
        self.assertEqual(Point(1,2) == Point(1, 2), True)
        self.assertEqual(Point(1,6) == Point(1, 2), False)

    def test_neq(self):
        self.assertEqual(Point(1,2) != Point(1, 4), True)
        self.assertEqual(Point(1,1) != Point(1, 1), False)

    def test_add(self):
        self.assertEqual(Point(1,2) + Point(1, 4), Point(2, 6))
        self.assertEqual(Point(1,2) + Point(-1, 4), Point(0, 6))

    def test_sub(self):
        self.assertEqual(Point(1,2) - Point(1, 4), Point(0, -2))
        self.assertEqual(Point(1,2) - Point(-1, 4), Point(2, -2))
        self.assertEqual(Point(0,0) - Point(-1, 0), Point(1, 0))

    def test_mul(self):
        self.assertEqual(Point(1,2) * Point(1, 4), Point(1, 8))
        self.assertEqual(Point(0,2) * Point(1, 0), Point(0, 0))

    def test_mul(self):
        self.assertEqual(Point(1,2) * Point(1, 4), Point(1, 8))
        self.assertEqual(Point(0,2) * Point(1, 0), Point(0, 0))


    def test_length(self):
        self.assertEqual(Point(1,2).length(), math.sqrt(5))
        self.assertEqual(Point(1,1).length(), math.sqrt(2))
        self.assertEqual(Point(0,1).length(), 1)
        self.assertEqual(Point(0,0).length(), 0)

    def test_cross(self):
        self.assertEqual(Point(1,2).cross(Point(1,2)), 0)
        self.assertEqual(Point(1,1).cross(Point(1,2)), 1)

if __name__ == '__main__':
    unittest.main()