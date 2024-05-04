import logging
import sys
import unittest
import time

from Day_6.day_6 import *

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
        logger.info('%s: %.6f' % (self.id(), t) + '\n')

    def test_first_answer_brut_test(self, path='race_test.txt'):
        result = first_answer_brut(path)
        self.assertEqual(288, result)
        logger.info(f'Test passed :: {result=}')

    def test_first_answer_brut(self, path='race.txt'):
        result = first_answer_brut(path)
        self.assertEqual(449550, result)
        logger.info(f'Test passed :: {result=}')

    def test_first_answer_test(self, path='race_test.txt'):
        result = first_answer(path)
        self.assertEqual(288, result)
        logger.info(f'Test passed :: {result=}')

    def test_first_answer(self, path='race.txt'):
        result = first_answer(path)
        self.assertEqual(449550, result)
        logger.info(f'Test passed :: {result=}')

    def test_second_answer_brut_test(self):
        result = len(second_answer(71530, 940200))
        self.assertEqual(71503, result)
        logger.info(f'Test passed :: {result=}')

    def test_second_answer_brut(self):
        result = len(second_answer(46828479, 347152214061471))
        self.assertEqual(28360140, result)
        logger.info(f'Test passed :: {result=}')

    def test_second_answer_test(self):
        result = len(win_ways(71530, 940200))
        self.assertEqual(71503, result)
        logger.info(f'Test passed :: {result=}')

    def test_second_answer(self):
        result = len(win_ways(46828479, 347152214061471))
        self.assertEqual(28360140, result)
        logger.info(f'Test passed :: {result=}')


if __name__ == '__main__':
    unittest.main()
