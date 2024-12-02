import unittest
import day_2
import time


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.5fs' % (self.id(), t))

    def test_task0_test(self):
        test_answer = day_2.task_0('test.txt')
        self.assertEqual(test_answer, 2)

    def test_task0(self):
        answer = day_2.task_0('input.txt')
        self.assertEqual(answer, 314)

    def test_task1_test(self):
        test_answer = day_2.task_1('test.txt')
        self.assertEqual(test_answer, 4)

    def test_task1(self):
        answer = day_2.task_1('input.txt')
        self.assertEqual(answer, 373)


if __name__ == '__main__':
    unittest.main()
