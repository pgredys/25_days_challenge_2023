import unittest

from Day_4.day_4 import first_answer
class MyTestCase(unittest.TestCase):
    def test_first_answer_test(self):
        results = first_answer('scratchcards_test.txt')
        self.assertEqual(13, results)  # add assertion here

    def test_first_answer_(self):
        results = first_answer('scratchcards.txt')
        self.assertEqual(21558, results)  # add assertion here


if __name__ == '__main__':
    unittest.main()
