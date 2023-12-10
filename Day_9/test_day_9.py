import unittest
from day_9 import first_answer,second_answer


class MyTestCase(unittest.TestCase):
    def test_part_1(self):
        answers = first_answer()
        self.assertEqual(114, answers[0])
        self.assertEqual(1992273652, answers[1])

    def test_part_2(self):
        answers = second_answer()
        self.assertEqual(2, answers[0])
        self.assertEqual(1012, answers[1])


if __name__ == '__main__':
    unittest.main()
