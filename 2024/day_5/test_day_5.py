import time
import unittest

import day_5

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.5fs' % (self.id(), t))

    def test_task0_test(self):
        test_answer = day_5.task_0('test.txt')
        self.assertEqual(test_answer, 143)

    def test_task0(self):
        answer = day_5.task_0('input.txt')
        self.assertEqual(answer, 5091)

    def test_task1_test(self):
        test_answer = day_5.task_1('test.txt')
        self.assertEqual(test_answer, 123)

    def test_task1(self):
        answer = day_5.task_1('input.txt')
        self.assertEqual(answer, 4681)

if __name__ == '__main__':
    unittest.main()
