from src.kyu_7.vowel_count import get_count
import unittest


class MyTestCase(unittest.TestCase):
    def test_vowel_count(self):
        self.assertEqual(get_count("abracadabra"), 5)

if __name__ == '__main__':
    unittest.main()
