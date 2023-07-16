import unittest

class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for number in nums:
            self.result += number
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for number in nums:
            self.result -= number
        return self


class TestMathDojo(unittest.TestCase):
    def setUp(self):
        self.md = MathDojo()

    def test_addition(self):
        self.assertEqual(self.md.add(2).add(2, 5, 1).result, 10)

    def test_subtraction(self):
        self.assertEqual(self.md.subtract(3, 2).result, 5)

    def test_combined_operations(self):
        self.assertEqual(self.md.add(2, 3).subtract(1, 2).result, 2)

if __name__ == '__main__':
    unittest.main()