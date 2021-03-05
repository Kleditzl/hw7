import unittest
import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
    def test_fizz_print(self):
        #self.assertEqual(fizzbuzz.fizz_print(), "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100")
        #self.assertEqual(fizzbuzz.fizz_print(), "1 2 fizz 4 5 fizz 7 8 fizz 10 11 fizz 13 14 fizz 16 17 fizz 19 20 fizz 22 23 fizz 25 26 fizz 28 29 fizz 31 32 fizz 34 35 fizz 37 38 fizz 40 41 fizz 43 44 fizz 46 47 fizz 49 50 fizz 52 53 fizz 55 56 fizz 58 59 fizz 61 62 fizz 64 65 fizz 67 68 fizz 70 71 fizz 73 74 fizz 76 77 fizz 79 80 fizz 82 83 fizz 85 86 fizz 88 89 fizz 91 92 fizz 94 95 fizz 97 98 fizz 100")
        #self.assertEqual(fizzbuzz.fizz_print(), "1 2 fizz 3 4 buzz fizz 6 7 8 fizz 9 buzz 11 fizz 12 13 14 fizz buzz 16 17 fizz 18 19 buzz fizz 21 22 23 fizz 24 buzz 26 fizz 27 28 29 fizz buzz 31 32 fizz 33 34 buzz fizz 36 37 38 fizz 39 buzz 41 fizz 42 43 44 fizz buzz 46 47 fizz 48 49 buzz fizz 51 52 53 fizz 54 buzz 56 fizz 57 58 59 fizz buzz 61 62 fizz 63 64 buzz fizz 66 67 68 fizz 69 buzz 71 fizz 72 73 74 fizz buzz 76 77 fizz 78 79 buzz fizz 81 82 83 fizz 84 buzz 86 fizz 87 88 89 fizz buzz 91 92 fizz 93 94 buzz fizz 96 97 98 fizz 99 buzz")
        self.assertEqual(fizzbuzz.fizz_print(), "1 2 fizz 3 4 buzz fizz 6 7 8 fizz 9 buzz 11 fizz 12 13 14 fizzbuzz 16 17 fizz 18 19 buzz fizz 21 22 23 fizz 24 buzz 26 fizz 27 28 29 fizzbuzz 31 32 fizz 33 34 buzz fizz 36 37 38 fizz 39 buzz 41 fizz 42 43 44 fizzbuzz 46 47 fizz 48 49 buzz fizz 51 52 53 fizz 54 buzz 56 fizz 57 58 59 fizzbuzz 61 62 fizz 63 64 buzz fizz 66 67 68 fizz 69 buzz 71 fizz 72 73 74 fizzbuzz 76 77 fizz 78 79 buzz fizz 81 82 83 fizz 84 buzz 86 fizz 87 88 89 fizzbuzz 91 92 fizz 93 94 buzz fizz 96 97 98 fizz 99 buzz")

if __name__ == '__main__':
    unittest.main()
