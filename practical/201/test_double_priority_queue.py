#!/usr/bin/python3

import unittest

from double_priority_queue import DoublePriorityQueue

class TestDoublePriorityQueue(unittest.TestCase):

    def test_countEmptyDpq(self):
        dpq = DoublePriorityQueue()
        expected = 0
        actual = dpq.Count()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
