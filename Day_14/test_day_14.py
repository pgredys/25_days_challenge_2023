import logging
import sys
import time
import unittest

from Day_14.day_14 import first_answer

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

    def test_first_answer_test(self):
        path = 'rocks_test.txt'
        ans = first_answer(path)
        self.assertEqual(ans, 136)

    def test_first_answer(self):
        path = 'rocks.txt'
        ans = first_answer(path)
        self.assertEqual(ans, 108641)


if __name__ == '__main__':
    unittest.main()
