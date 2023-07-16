import unittest

def reverseList(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

class TestReverseList(unittest.TestCase):
    def test_reverse_list(self):
        # Test case 1
        arr = [1, 3, 5]
        self.assertEqual(reverseList(arr), [5, 3, 1])

        # Test case 2
        arr = [4, 6, 8, 10]
        self.assertEqual(reverseList(arr), [10, 8, 6, 4])

        # Test case 3
        arr = []
        self.assertEqual(reverseList(arr), [])

if __name__ == '__main__':
    unittest.main()


def isPalindrome(word):
    return word == word[::-1]

class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        # Test case 1
        word = "racecar"
        self.assertTrue(isPalindrome(word))

        # Test case 2
        word = "hello"
        self.assertFalse(isPalindrome(word))

        # Test case 3
        word = "madam"
        self.assertTrue(isPalindrome(word))

        # Test case 4
        word = "level"
        self.assertTrue(isPalindrome(word))

        # Test case 5
        word = "python"
        self.assertFalse(isPalindrome(word))

if __name__ == '__main__':
    unittest.main()


def coins(cents):
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    cents %= 5
    pennies = cents

    return [quarters, dimes, nickels, pennies]

class TestCoins(unittest.TestCase):
    def test_coins(self):
        # Test case 1
        cents = 87
        self.assertEqual(coins(cents), [3, 1, 0, 2])

        # Test case 2
        cents = 123
        self.assertEqual(coins(cents), [4, 2, 0, 3])

        # Test case 3
        cents = 0
        self.assertEqual(coins(cents), [0, 0, 0, 0])

        # Test case 4
        cents = 10
        self.assertEqual(coins(cents), [0, 1, 0, 0])

        # Test case 5
        cents = 99
        self.assertEqual(coins(cents), [3, 2, 0, 4])

if __name__ == '__main__':
    unittest.main()


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        # Test case 1
        n = 5
        self.assertEqual(factorial(n), 120)

        # Test case 2
        n = 0
        self.assertEqual(factorial(n), 1)

        # Test case 3
        n = 10
        self.assertEqual(factorial(n), 3628800)

if __name__ == '__main__':
    unittest.main()


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        # Test case 1
        n = 5
        self.assertEqual(fibonacci(n), 5)

        # Test case 2
        n = 4
        self.assertEqual(fibonacci(n), 3)

        # Test case 3
        n = 10
        self.assertEqual(fibonacci(n), 55)

if __name__ == '__main__':
    unittest.main()
