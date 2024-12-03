import unittest
import time
import day_3

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.5fs' % (self.id(), t))

    def test_task0_test(self):
        test_answer = day_3.task_0('test.txt')
        self.assertEqual(test_answer, 161)

    def test_task0(self):
        answer = day_3.task_0('input.txt')
        self.assertEqual(answer, 196826776)

    def test_task1_test(self):
        test_answer = day_3.task_1('test2.txt')
        self.assertEqual(test_answer, 48)

    def test_task1(self):
        answer = day_3.task_1('input.txt')
        self.assertEqual(answer, 106780429)


if __name__ == '__main__':
    unittest.main()
