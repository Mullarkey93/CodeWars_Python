from src.kyu_7.number import number
import unittest


class MyTestCase(unittest.TestCase):
    def test_vowel_count(self):
        self.assertEqual(number([]), [])
        self.assertEqual(number(["a", "b", "c"]), ["1: a", "2: b", "3: c"])


if __name__ == '__main__':
    unittest.main()
