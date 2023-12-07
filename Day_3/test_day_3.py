import unittest

from Day_3.day_3 import first_answer


class MyTestCase(unittest.TestCase):
    def test_first_answer_test(self):
        path = 'engine_test.txt'
        answer = first_answer(path)
        self.assertEqual(4361, answer)

    def test_first_answer(self):
        path = 'engine.txt'
        answer = first_answer(path)
        self.assertEqual(531932, answer)


if __name__ == '__main__':
    unittest.main()
