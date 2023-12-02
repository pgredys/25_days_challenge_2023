import unittest
from Day_1.src.day_1 import *


class Day1A(unittest.TestCase):

    def test_example(self):
        imported_lines = import_lines("..\\src\\Trebuchet_test.txt")
        results = 0
        for index, line in enumerate(imported_lines):
            digits = find_digits(line)
            number = decode_number(digits)
            self.assertIsInstance(number, int)
            self.assertTrue(11 <= number <= 99)

            results += number

        self.assertIsInstance(results, int)
        self.assertEqual(results, 142)

    def test_final(self):
        imported_lines = import_lines("..\\src\\Trebuchet.txt")
        results = 0
        for index, line in enumerate(imported_lines):
            digits = find_digits(line)
            number = decode_number(digits)
            results += number
        self.assertEqual(results, 55834)


class Day1B(unittest.TestCase):
    def test_example(self):
        lines = import_lines("..\\src\\Trebuchet_test.txt")
        results = 0
        for index, line in enumerate(lines):
            new_line = decode_line(line)

            digits = find_digits(new_line)
            number = decode_number(digits)

            print(f'{line.strip()}::{new_line.strip()}::{number}')
            results += number

        self.assertEqual(142, results)

    def test_final(self):
        lines = import_lines("..\\src\\Trebuchet.txt")
        results = 0
        for index, line in enumerate(lines):
            new_line = decode_line(line)

            digits = find_digits(new_line)
            number = decode_number(digits)

            print(f'{line.strip()}::{new_line.strip()}::{number}')
            results += number
        self.assertEqual(53221, results)


if __name__ == '__main__':
    unittest.main()
