#!/usr/bin/python3

import unittest

from double_priority_queue import DoublePriorityQueue

class TestDoublePriorityQueue(unittest.TestCase):

    def test_countEmpty(self):
        dpq = DoublePriorityQueue()
        expected = 0
        actual = dpq.Count()
        self.assertEqual(expected, actual)

    def test_countSingleNode(self):
        dpq = DoublePriorityQueue()
        string = "Alice"
        priorityA = 1.23
        priorityB = 4.56
        dpq.Enqueue(string, priorityA, priorityB)
        expected = 1
        actual = dpq.Count()
        self.assertEqual(expected, actual)
    
if __name__ == "__main__":
    unittest.main()
