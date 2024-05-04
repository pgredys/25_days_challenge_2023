import logging
import time
import unittest

from Day_16.day_16 import *

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
        path = 'layout_test.txt'
        grid = import_grid(path)
        ans = illuminated_from((0, 0, 'R'), grid)
        self.assertEqual(46, ans)

    def test_first(self):
        path = 'layout.txt'
        grid = import_grid(path)
        ans = illuminated_from((0, 0, 'R'), grid)
        self.assertEqual(7496, ans)

    def test_second_test(self):
        path = 'layout_test.txt'
        grid = import_grid(path)
        possibilities = start_possibilities(len(grid), len(grid[0]))
        ans = max(illuminated_from(test, grid) for test in possibilities)
        self.assertEqual(51, ans)

    def test_second(self):
        path = 'layout.txt'
        grid = import_grid(path)
        possibilities = start_possibilities(len(grid), len(grid[0]))
        ans = max(illuminated_from(test, grid) for test in possibilities)
        self.assertEqual(7932, ans)


if __name__ == '__main__':
    unittest.main()
