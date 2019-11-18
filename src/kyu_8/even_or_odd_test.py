import unittest
from src.kyu_8.even_or_odd import even_or_odd


class MyTestCase(unittest.TestCase):

    def test_even_or_odd(self):
        self.assertEqual(even_or_odd(2), "Even")
        self.assertEqual(even_or_odd(0), "Even")
        self.assertEqual(even_or_odd(7), "Odd")
        self.assertEqual(even_or_odd(1), "Odd")
        self.assertEqual(even_or_odd(-1), "Odd")


if __name__ == '__main__':
    unittest.main()