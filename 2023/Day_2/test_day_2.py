import unittest
from Day_2.day_2 import first_answer,second_answer


class TestDay2(unittest.TestCase):

    def test_first_task_test(self, file_path='games_test.txt'):
        constraints = {'red': 12, 'blue': 14, 'green': 13}
        result = first_answer(file_path, constraints)
        self.assertEqual(8, result)

    def test_first_task(self, file_path='games.txt'):
        constraints = {'red': 12, 'blue': 14, 'green': 13}
        result = first_answer(file_path, constraints)
        self.assertEqual(2162, result)

    def test_second_task_test(self, file_path='games_test.txt'):
        result = second_answer(file_path)
        self.assertEqual(2286, result)

    def test_second_task(self, file_path='games.txt'):
        result = second_answer(file_path)
        self.assertEqual(72513, result)


if __name__ == '__main__':
    unittest.main()
