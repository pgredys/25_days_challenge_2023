import logging
import sys
import time
import unittest

from Day_15.day_15 import first_answer, second_answer

logger = logging.getLogger(__name__)
logging.disable(logging.NOTSET)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.startTime = time.time()
        logger.info('%s: Test started' % self.id())

    def tearDown(self):
        t = time.time() - self.startTime
        logger.info('%s: %.9f' % (self.id(), t) + '\n')

    def test_first_test(self):
        path = 'sequence_test.txt'
        ans = first_answer(path)
        self.assertEqual(ans, 1320)

    def test_first(self):
        path = 'sequence.txt'
        ans = first_answer(path)
        self.assertEqual(ans, 503487)

    def test_second_test(self):
        path = 'sequence_test.txt'
        ans = second_answer(path)
        self.assertEqual(ans, 145)

    def test_second(self):
        path = 'sequence.txt'
        ans = second_answer(path)
        self.assertEqual(ans, 261505)


if __name__ == '__main__':
    unittest.main()
