import unittest
import katas
import math

class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(1, 2), 3)

    def test_multiply(self):
        self.assertEqual(katas.multiply(3,4), 12)

    def test_power(self):
        self.assertEqual(katas.power(1, 4), math.pow(1, 4) )

    def test_factorial(self):
        self.assertEqual(katas.factorial(5), math.factorial(5))

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(9), 21)


if __name__ == '__main__':
    unittest.main()
