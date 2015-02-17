#!/usr/bin/python3

import unittest

from double_priority_queue import DoublePriorityQueue

class TestDoublePriorityQueue(unittest.TestCase):

    def test_countEmpty(self):
        dpq = DoublePriorityQueue()
        expected = 0
        actual = dpq.Count()
        self.assertEqual(expected, actual)

    def test_countOneNode(self):
        dpq = DoublePriorityQueue()
        string = "Alice"
        priorityA = 1.23
        priorityB = 4.56
        dpq.Enqueue(string, priorityA, priorityB)
        expected = 1
        actual = dpq.Count()
        self.assertEqual(expected, actual)

    def test_countTwoNodes(self):
        dpq = DoublePriorityQueue()
        string1 = "Alice"
        priorityA1 = 1.23
        priorityB1 = 4.56
        dpq.Enqueue(string1, priorityA1, priorityB1)
        string2 = "Bob"
        priorityA2 = 7.89
        priorityB2 = 0.12
        dpq.Enqueue(string2, priorityA2, priorityB2)
        expected = 2
        actual = dpq.Count()
        self.assertEqual(expected, actual)
    
if __name__ == "__main__":
    unittest.main()
