import unittest
import leap_year

class TestLeapYear(unittest.TestCase):
    def test_ly(self):
        self.assertEqual(leap_year.ly(4), True)
        self.assertEqual(leap_year.ly(100), False)
        
if __name__ == '__main__':
    unittest.main()