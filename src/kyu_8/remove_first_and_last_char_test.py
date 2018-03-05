from src.kyu_8.remove_first_and_last_char import remove_char
import unittest


class MyTestCase(unittest.TestCase):
    def test_first_and_last(self):
        self.assertEqual(remove_char('eloquent'), 'loquen')
        self.assertEqual(remove_char('country'), 'ountr')
        self.assertEqual(remove_char('person'), 'erso')
        self.assertEqual(remove_char('place'), 'lac')
        self.assertEqual(remove_char('ok'), '')

if __name__ == '__main__':
    unittest.main()