import pytest
from points import Point
from rectangles import Rectangle

def test_constructor():
    with pytest.raises(ValueError):
        Rectangle(0, 0, -1, -1)
    with pytest.raises(ValueError):
        Rectangle(0, 0, -1, 1)
    with pytest.raises(ValueError):
        Rectangle(0, 0, 1, -1)

def test_str():
    rect = Rectangle(1, 1, 2, 2)
    assert str(rect) == f'[({rect.pt1.x}, {rect.pt1.y}), ({rect.pt2.x}, {rect.pt2.y})]'

def test_repr():
    rect = Rectangle(1, 1, 2, 2)
    assert repr(rect) == f'Rectangle({rect.pt1.x}, {rect.pt1.y}, {rect.pt2.x}, {rect.pt2.y})'

def test_eq():
    rect = Rectangle(1, 1, 2, 2)
    rect1 = Rectangle(1, 1, 2, 2)
    assert rect == rect1

    rect = Rectangle(0, 0, 1, 1)
    rect1 = Rectangle(1, 1, 2, 2)
    assert rect == rect1

def test_ne():
    rect = Rectangle(1, 1, 2, 3)
    rect1 = Rectangle(1, 1, 2, 2)
    assert rect != rect1

    rect = Rectangle(0, 0, 1, 1)
    rect1 = Rectangle(1, 1, 2, 3)
    assert rect != rect1


def test_center():
    rect = Rectangle(0, 0, 1, 1)
    assert rect.center() == (0.5, 0.5)

    rect = Rectangle(-1, -1, 1, 1)
    assert rect.center() == (0, 0)

def test_area():
    rect = Rectangle(0, 0, 1, 1)
    assert rect.area() == 1
    assert rect.area() == 1.0

    rect = Rectangle(-1, -1, 1, 1)
    assert rect.area() == 4
    assert rect.area() == 4.0

def test_move():
    rect = Rectangle(0, 0, 1, 1)
    rect.move(1, 1)
    expected = Rectangle(1, 1, 2, 2)
    assert rect == expected

    rect = Rectangle(-1, -1, 1, 1)
    rect.move(-1, -1)
    expected = Rectangle(-2, -2, 0, 0)
    assert rect == expected

    rect = Rectangle(-1, -1, 1, 1)
    rect.move(-1, 1)
    expected = Rectangle(-2, 0, 0, 2)
    assert rect == expected

def test_from_points_throws():
    with pytest.raises(ValueError):
        point1 = Point(0, 0)
        point2 = Point(-1, -1)
        Rectangle.from_points((point1, point2))

    with pytest.raises(ValueError):
        point1 = Point(0, 0)
        point2 = Point(-1, 1)
        Rectangle.from_points((point1, point2))

    with pytest.raises(ValueError):
        point1 = Point(0, 0)
        point2 = Point(1, -1)
        Rectangle.from_points((point1, point2))

def test_from_points():
    point1 = Point(0, 0)
    point2 = Point(1, 1)
    assert Rectangle.from_points((point1, point2)) == Rectangle(0, 0, 1, 1)

def test_number_props():
    rect = Rectangle(-1, -1, 1, 1)
    assert rect.top == 1
    assert rect.left == -1
    assert rect.right == 1
    assert rect.bottom == -1
    assert rect.width == 2
    assert rect.height == 2

def test_point_props():
    rect = Rectangle(-1, -1, 1, 1)
    assert rect.topleft == Point(-1, 1)
    assert rect.topright == Point(1, 1)
    assert rect.bottomleft == Point(-1, -1)
    assert rect.bottomright == Point(1, -1)