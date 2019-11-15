from src.kyu_8.past import past
import unittest


class MyTestCase(unittest.TestCase):
    def test_past(self):
        self.assertEqual(past(0, 1, 1), 61000)
        self.assertEqual(past(1, 1, 1), 3661000)
        self.assertEqual(past(0, 0, 0), 0)
        self.assertEqual(past(1, 0, 1), 3601000)
        self.assertEqual(past(1, 0, 0), 3600000)


if __name__ == '__main__':
    unittest.main()