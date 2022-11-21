from math import gcd

def simplify(frac):
    common_divisor = gcd(frac[0], frac[1])
    return [int(frac[0]/common_divisor), int(frac[1]/common_divisor)]

def add_frac(frac1, frac2):
    numenator_1 = frac1[0] * frac2[1]
    denominator = frac1[1] * frac2[1]
    numenator_2 = frac1[1] * frac2[0]

    numenator_result = numenator_1 + numenator_2
    if numenator_result == 0:
        return 0

    return simplify([numenator_result, denominator])



def sub_frac(frac1, frac2):
    numenator_1 = frac1[0] * frac2[1]
    denominator = frac1[1] * frac2[1]
    numenator_2 = frac1[1] * frac2[0]

    numenator_result = numenator_1 - numenator_2
    if numenator_result == 0:
        return 0

    return simplify([numenator_result, denominator])

def mul_frac(frac1, frac2):
    result = simplify([frac1[0] * frac2[0], frac1[1] * frac2[1]])
    
    if result[0] == 0:
        return 0

    return result

def div_frac(frac1, frac2):
    if frac2[0] == 0:
        raise ZeroDivisionError

    frac2 = [frac2[1], frac2[0]]
    result = simplify(mul_frac(frac1, frac2))
    if result[0] == 0:
        return 0

    return result

def is_positive(frac):
    return (frac[0] * frac[1]) > 0

def is_zero(frac):               
    return frac[0] == 0

def frac2float(frac):
    if frac[1] == 0:
        raise ZeroDivisionError

    return frac[0]/frac[1]

def cmp_frac(frac1, frac2):        # -1 | 0 | +1
    fl_1 = frac2float(frac1)
    fl_2 = frac2float(frac2)

    if fl_1 == fl_2:
        return 0

    if fl_1 > fl_2:
        return 1
    
    return -1

# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 100], [1,100]), [1, 50])
        self.assertEqual(add_frac([0, 2], [0, 420]), 0)

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([1, 2], [1, 2]), 0)

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 2]), [1, 4])
        self.assertEqual(mul_frac([1, 2], [0, 2]), 0)

    def test_div_frac(self):
        with self.assertRaises(ZeroDivisionError):
            div_frac([1, 2], [0, 2])

    def test_is_positive(self):
        self.assertEqual(is_positive([-1, -2]), True)
        self.assertEqual(is_positive([1, -2]), False)
        self.assertEqual(is_positive([-1, 2]), False)
        self.assertEqual(is_positive([1, 2]), True)
        self.assertEqual(is_positive([0, -2]), False)

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 1]), True)
        self.assertEqual(is_zero([0, -1]), True)

    def test_cmp_frac(self):
        self.assertTrue(cmp_frac([0, 1], [1,1]) < 0)
        self.assertTrue(cmp_frac([0, -1], [-1,-2]) < 0)
        self.assertTrue(cmp_frac([100, 1], [1,1]) > 0)
        self.assertTrue(cmp_frac([-100, -1], [1,1]) > 0)
        self.assertTrue(cmp_frac([-100, -100], [-1,-1]) == 0)
        self.assertTrue(cmp_frac([-1, 2], [1,-2]) == 0)

    def test_frac2float(self):
        self.assertEqual(frac2float([1,2]), 0.5)
        self.assertEqual(frac2float([1,4]), 0.25)
        self.assertEqual(frac2float([1,-4]), -0.25)
        self.assertEqual(frac2float([0,-4]), 0)
        with self.assertRaises(ZeroDivisionError):
            frac2float([1, 0])

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()