import time
import unittest
import day_1

class Day1(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.5fs' % (self.id(), t))

    def test_task0_test(self):
        test_answer = day_1.task_0('test.txt')
        self.assertEqual(test_answer, 11)

    def test_task0(self):
        answer = day_1.task_0('input.txt')
        self.assertEqual(answer, 1660292)

    def test_task1_test(self):
        test_answer = day_1.task_1('test.txt')
        self.assertEqual(test_answer, 31)

    def test_task1(self):
        answer = day_1.task_1('input.txt')
        self.assertEqual(answer, 22776016)


if __name__ == '__main__':
    unittest.main()
