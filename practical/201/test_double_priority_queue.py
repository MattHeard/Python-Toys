#!/usr/bin/python3

import unittest

from double_priority_queue import DoublePriorityQueue

class TestDoublePriorityQueue(unittest.TestCase):
    """The test suite for DoublePriorityQueue."""

    def test_countEmpty(self):
        """Test counting an empty DPQ."""
        dpq = DoublePriorityQueue()
        expected = 0
        actual = dpq.Count()
        self.assertEqual(expected, actual)

    def test_countOneNode(self):
        """Test counting a DPQ with one entry."""
        dpq = DoublePriorityQueue()
        string = "Alice"
        priorityA = 1.23
        priorityB = 4.56
        dpq.Enqueue(string, priorityA, priorityB)
        expected = 1
        actual = dpq.Count()
        self.assertEqual(expected, actual)

    def test_countTwoNodes(self):
        """Test counting a DPQ with two entries."""
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

    def test_popQueueOnce(self):
        """Test popping the queue in a DPQ once."""
        dpq = DoublePriorityQueue()
        string = "Alice"
        priorityA = 1.23
        priorityB = 4.56
        dpq.Enqueue(string, priorityA, priorityB)
        expected = 1
        actual = dpq.Count()
        self.assertEqual(expected, actual)
        expected = ("Alice", 1.23, 4.56)
        actual = dpq.Dequeue()
        self.assertEqual(expected, actual)
        expected = 0
        actual = dpq.Count()
        self.assertEqual(expected, actual)

    def test_popQueueTwice(self):
        """Test popping the queue in a DPQ twice."""
        dpq = DoublePriorityQueue()
        string1 = "Alice"
        priorityA1 = 1.23
        priorityB1 = 4.56
        dpq.Enqueue(string1, priorityA1, priorityB1)
        expected = 1
        actual = dpq.Count()
        self.assertEqual(expected, actual)
        string2 = "Bob"
        priorityA2 = 7.89
        priorityB2 = 0.12
        dpq.Enqueue(string2, priorityA2, priorityB2)
        expected = 2
        actual = dpq.Count()
        self.assertEqual(expected, actual)
        expected = ("Alice", 1.23, 4.56)
        actual = dpq.Dequeue()
        self.assertEqual(expected, actual)
        expected = 1
        actual = dpq.Count()
        self.assertEqual(expected, actual)
        expected = ("Bob", 7.89, 0.12)
        actual = dpq.Dequeue()
        self.assertEqual(expected, actual)
        expected = 0
        actual = dpq.Count()
        self.assertEqual(expected, actual)

    def test_popQueueThrice(self):
        """Test popping the queue in a DPQ thrice."""
        dpq = DoublePriorityQueue()
        string1 = "Alice"
        priorityA1 = 1.23
        priorityB1 = 4.56
        dpq.Enqueue(string1, priorityA1, priorityB1)
        expected = 1
        actual = dpq.Count()
        self.assertEqual(expected, actual)
        string2 = "Bob"
        priorityA2 = 7.89
        priorityB2 = 0.12
        dpq.Enqueue(string2, priorityA2, priorityB2)
        expected = 2
        actual = dpq.Count()
        self.assertEqual(expected, actual)
        string3 = "Charlie"
        priorityA3 = 3.45
        priorityB3 = 6.78
        dpq.Enqueue(string3, priorityA3, priorityB3)
        expected = 3
        actual = dpq.Count()
        self.assertEqual(expected, actual)
        expected = ("Alice", 1.23, 4.56)
        actual = dpq.Dequeue()
        self.assertEqual(expected, actual)
        expected = 2
        actual = dpq.Count()
        self.assertEqual(expected, actual)
        expected = ("Bob", 7.89, 0.12)
        actual = dpq.Dequeue()
        self.assertEqual(expected, actual)
        expected = 1
        actual = dpq.Count()
        self.assertEqual(expected, actual)
        expected = ("Charlie", 3.45, 6.78)
        actual = dpq.Dequeue()
        self.assertEqual(expected, actual)
        expected = 0
        actual = dpq.Count()
        self.assertEqual(expected, actual)

    def test_popPriorityQueueAOnce(self):
        """Test popping the first priority queue in a DPQ once."""
        dpq = DoublePriorityQueue()
        string = "Alice"
        priorityA = 1.23
        priorityB = 4.56
        dpq.Enqueue(string, priorityA, priorityB)
        expected = 1
        actual = dpq.Count()
        self.assertEqual(expected, actual)
        expected = ("Alice", 1.23, 4.56)
        actual = dpq.DequeueA()
        self.assertEqual(expected, actual)
        expected = 0
        actual = dpq.Count()
        self.assertEqual(expected, actual)

    def test_popPriorityQueueATwice(self):
        """Test popping the first priority queue in a DPQ twice."""
        dpq = DoublePriorityQueue()
        string1 = "Alice"
        priorityA1 = 1.23
        priorityB1 = 4.56
        dpq.Enqueue(string1, priorityA1, priorityB1)
        expected = 1
        actual = dpq.Count()
        self.assertEqual(expected, actual)
        string2 = "Bob"
        priorityA2 = 7.89
        priorityB2 = 0.12
        dpq.Enqueue(string2, priorityA2, priorityB2)
        expected = 2
        actual = dpq.Count()
        self.assertEqual(expected, actual)
        expected = ("Bob", 7.89, 0.12)
        actual = dpq.DequeueA()
        self.assertEqual(expected, actual)
        expected = 1
        actual = dpq.Count()
        self.assertEqual(expected, actual)
        expected = ("Alice", 1.23, 4.56)
        actual = dpq.DequeueA()
        self.assertEqual(expected, actual)
        expected = 0
        actual = dpq.Count()
        self.assertEqual(expected, actual)
    
    def test_popPriorityQueueBOnce(self):
        """Test popping the second priority queue in a DPQ once."""
        dpq = DoublePriorityQueue()
        string = "Alice"
        priorityA = 1.23
        priorityB = 4.56
        dpq.Enqueue(string, priorityA, priorityB)
        expected = 1
        actual = dpq.Count()
        self.assertEqual(expected, actual)
        expected = ("Alice", 1.23, 4.56)
        actual = dpq.DequeueB()
        self.assertEqual(expected, actual)
        expected = 0
        actual = dpq.Count()
        self.assertEqual(expected, actual)

    def test_popPriorityQueueBTwice(self):
        """Test popping the second priority queue in a DPQ twice."""
        dpq = DoublePriorityQueue()
        string1 = "Alice"
        priorityA1 = 1.23
        priorityB1 = 4.56
        dpq.Enqueue(string1, priorityA1, priorityB1)
        expected = 1
        actual = dpq.Count()
        self.assertEqual(expected, actual)
        string2 = "Bob"
        priorityA2 = 7.89
        priorityB2 = 0.12
        dpq.Enqueue(string2, priorityA2, priorityB2)
        expected = 2
        actual = dpq.Count()
        self.assertEqual(expected, actual)
        expected = ("Alice", 1.23, 4.56)
        actual = dpq.DequeueB()
        self.assertEqual(expected, actual)
        expected = 1
        actual = dpq.Count()
        self.assertEqual(expected, actual)
        expected = ("Bob", 7.89, 0.12)
        actual = dpq.DequeueB()
        self.assertEqual(expected, actual)
        expected = 0
        actual = dpq.Count()
        self.assertEqual(expected, actual)

    def test_clear(self):
        """Test clearing a DPQ."""
        dpq = DoublePriorityQueue()
        string1 = "Alice"
        priorityA1 = 1.23
        priorityB1 = 4.56
        dpq.Enqueue(string1, priorityA1, priorityB1)
        expected = 1
        actual = dpq.Count()
        self.assertEqual(expected, actual)
        string2 = "Bob"
        priorityA2 = 7.89
        priorityB2 = 0.12
        dpq.Enqueue(string2, priorityA2, priorityB2)
        expected = 2
        actual = dpq.Count()
        self.assertEqual(expected, actual)
        dpq.Clear()
        expected = 0
        actual = dpq.Count()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    """Run the unit tests."""
    unittest.main()
