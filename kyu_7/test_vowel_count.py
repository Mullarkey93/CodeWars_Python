from kyu_7.vowel_count import getCount
import unittest


class MyTestCase(unittest.TestCase):
    def test_vowel_count(self):
        self.assertEqual(getCount("abracadabra"), 5)

if __name__ == '__main__':
    unittest.main()
