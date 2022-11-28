from math import gcd


class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError("denominator can't be 0")
        self.x = x
        self.y = y

    def get_numenators(self, other):
        numenator_1 = self.x * other.y
        numenator_2 = self.y * other.x
        return (numenator_1, numenator_2)
    
    @classmethod
    def simplify(cls, frac):
        common_divisor = gcd(frac.x, frac.y)
        return cls(int(frac.x/common_divisor), int(frac.y/common_divisor))
    
    @classmethod
    def from_number(cls, number):
        if isinstance(number, (int, float)):
            ratio = float.as_integer_ratio(float(number))
            frac = Frac(ratio[0], ratio[1])
            return frac
        else:
            raise ValueError("Argument should be of type int | float")
        
    @classmethod
    def parse(cls, obj):
        if isinstance(obj, (int, float)):
            ratio = float.as_integer_ratio(float(obj))
            frac = Frac(ratio[0], ratio[1])
            return frac
        elif isinstance(obj, (Frac)):
            return obj
        else:
            raise ValueError("Argument should be of type int | float | Frac")

    def __str__(self):
        if self.y == 1:
            return str(self.x)
        return f'{self.x}/{self.y}'
        

    def __repr__(self):
        return f'Frac({self.x}, {self.y})'

    def __eq__(self, other):
        numenator_1, numenator_2 = self.get_numenators(other)
        return numenator_1 == numenator_2

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        numenator_1, numenator_2 = self.get_numenators(other)
        return numenator_1 < numenator_2

    def __le__(self, other):
        numenator_1, numenator_2 = self.get_numenators(other)
        return numenator_1 <= numenator_2

    def __add__(self, other):
        other = Frac.parse(other)
        numenator_1 = self.x * other.y
        denominator = self.y * other.y
        numenator_2 = self.y * other.x

        numenator_result = numenator_1 + numenator_2
        if numenator_result == 0:
            return 0

        return Frac.simplify(Frac(numenator_result, denominator))

    __radd__ = __add__            

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):      
        return (-self) + other

    def __mul__(self, other):
        other = Frac.parse(other)

        result = Frac.simplify(Frac(self.x * other.x, self.y * other.y))
    
        if result.x == 0:
            return 0

        return result

    __rmul__ = __mul__    

    def __truediv__(self, other):
        other = Frac.parse(other)
        if other.x == 0:
            raise ZeroDivisionError
        
        return self * (~other)

    def __rtruediv__(self, other):
        if self.x == 0:
            raise ZeroDivisionError
        
        other = Frac.parse(other)
        return (~self) * other

    # operatory jednoargumentowe
    def __pos__(self):
        return self

    def __neg__(self): #
        return Frac(self.x, -self.y)

    def __invert__(self): #
        return Frac(self.y, self.x)

    def __float__(self): #
        return float(self.x)/(self.y)

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # w Pythonie set([2]) == set([2.0])
        # chcemy set([2]) == set([Frac(2)])

# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase):
    def test_ctor(self):
        with self.assertRaises(ValueError):
            Frac(1, 0)

    def test_str(self):
        self.assertEqual(str(Frac(1, 2)), "1/2")
        self.assertEqual(str(Frac(1, 1)), "1")

    def test_repr(self):
        self.assertEqual(repr(Frac(1, 2)), "Frac(1, 2)")
        self.assertEqual(repr(Frac(1, 1)), "Frac(1, 1)")

    def test_eq(self):
        self.assertEqual(Frac(1, 2) == Frac(1, 2), True)
        self.assertEqual(Frac(1, 1) == Frac(2, 2), True)

    def test_ne(self):
        self.assertEqual(Frac(1, 2) != Frac(1, 3), True)
        self.assertEqual(Frac(1, 1) != Frac(2, 2), False)

    def test_lt(self):
        self.assertEqual(Frac(1, 3) < Frac(1, 2), True)
        self.assertEqual(Frac(1, 1) < Frac(2, 2), False)
        self.assertEqual(Frac(0, 1) < Frac(1, 1), True)

    def test_le(self):
        self.assertEqual(Frac(1, 3) <= Frac(1, 2), True)
        self.assertEqual(Frac(1, 1) <= Frac(2, 2), True)
        self.assertEqual(Frac(0.9, 1) <= Frac(2, 2), True)
        self.assertEqual(Frac(0, 1) <= Frac(1, 1), True)

    def test_add(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 2), Frac(1, 1))
        self.assertEqual(Frac(1, 5) + Frac(1, 5), Frac(2, 5))
        self.assertEqual(Frac(1, 5) + Frac(-1, 5), 0)
        self.assertEqual(Frac(1, 2) + 1, Frac(3, 2))
        self.assertEqual(1 + Frac(1, 2), Frac(3, 2))
        self.assertEqual(-1 + Frac(1, 2), Frac(1, -2))
        self.assertEqual(-1 + Frac(1, 2), Frac(-1, 2))

    def test_sub(self):
        self.assertEqual(Frac(1, 2) - Frac(1, 2), 0)
        self.assertEqual(Frac(1, 2) - Frac(1, 4), Frac(1, 4))
        self.assertEqual(Frac(3, 2) - 1, Frac(1, 2))
        self.assertEqual(1 - Frac(3, 2), Frac(-1, 2))
        self.assertEqual(1 - Frac(3, 2), Frac(1, -2))

    def test_mul(self):
        self.assertEqual(Frac(1, 2) * Frac(1, 4), Frac(1, 8))
        self.assertEqual(Frac(1, 4) * Frac(1, 2), Frac(1, 8))
        self.assertEqual(Frac(0, 4) * Frac(1, 2), 0)
        self.assertEqual(Frac(1, 4) * Frac(0, 2), 0)
        self.assertEqual(Frac(1, 4) * 2, Frac(1, 2))
        self.assertEqual(2 * Frac(1, 4), Frac(1, 2))

    def test_div(self):
        self.assertEqual(Frac(1, 2) / Frac(1, 2), Frac(1, 1))
        self.assertEqual(Frac(1, 4) / Frac(1, 8), Frac(2, 1))
        self.assertEqual(Frac(1, 4) / 2, Frac(1, 8))
        self.assertEqual(Frac(1, 8) / 2, Frac(1, 16))
        self.assertEqual(2 / Frac(1, 4), Frac(8, 1))

        with self.assertRaises(ZeroDivisionError):
            Frac(1, 1) / 0
        
        with self.assertRaises(ZeroDivisionError):
            Frac(1, 1) / Frac(0, 1)
        
    def test_invert(self):
        self.assertEqual(~Frac(1, 2), Frac(2, 1))

    def test_from_number(self):
        self.assertEqual(Frac.from_number(1.5), Frac(3, 2))
        self.assertEqual(Frac.from_number(100.5), Frac(201, 2))

if __name__ == '__main__':
    unittest.main()