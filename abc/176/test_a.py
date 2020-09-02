from a import calc
import unittest

class TestCalc(unittest.TestCase):

    def test_calc(self):
        self.assertEqual(calc(20, 12, 6), 12)
        self.assertEqual(calc(1000, 1, 1000), 1000000)

if __name__ == "__main__":
    unittest.main()