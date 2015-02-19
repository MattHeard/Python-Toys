from collections import deque, namedtuple

class DoublePriorityQueue:
    """A double priority queue, which looks the same as a regular priority
    queue, but uses two independent priorities instead of one. The double
    priority queue can either 'pop' the entry with the highest priority for
    'priority A', the entry with the highest priority for 'priority B', or the
    entry that was pushed on earliest (as in a regular queue)."""

    Node = namedtuple('Node', ['val', 'priorityA', 'priorityB'])

    def __init__(self):
        """Initialise the double priority queue."""
        self.queue = deque()
        self.priorityAList = []
        self.priorityBList = []

    def Count(self):
        """Return the number of entries."""
        return len(self.queue)

    def Clear(self):
        """Remove all entries from the double priority queue."""
        self.queue.clear()
        self.priorityAList.clear()
        self.priorityBList.clear()

    def pushOntoPriorityAList(self, node):
        """Push an entry onto priority list A."""
        pos = 0
        isAdded = False
        for curr in self.priorityAList:
            if node.priorityA > curr.priorityA:
                self.priorityAList.insert(pos, node)
                isAdded = True
                break
            else:
                pos += 1
        if isAdded == False:
            self.priorityAList.append(node)

    def pushOntoPriorityBList(self, node):
        """Push an entry onto priority list B."""
        isAdded = False
        pos = 0
        for curr in self.priorityBList:
            if node.priorityB > curr.priorityB:
                self.priorityBList.insert(pos, node)
                isAdded = True
                break
            else:
                pos += 1
        if isAdded == False:
            self.priorityBList.append(node)

    def Enqueue(self, val, priorityA, priorityB):
        """Push an entry onto the double priority queue."""
        node = self.Node(val, priorityA, priorityB)
        self.queue.append(node)
        self.pushOntoPriorityAList(node)
        self.pushOntoPriorityBList(node)

    def Dequeue(self):
        """Pop off the entry that was pushed on the earliest."""
        if len(self.queue) > 0:
            node = self.queue.popleft()
            self.priorityAList.remove(node)
            self.priorityBList.remove(node)
            return node
        else:
            return None

    def DequeueA(self):
        """Pop off the entry with the highest priority A."""
        if len(self.queue) > 0:
            node = self.priorityAList.pop(0)
            self.queue.remove(node)
            self.priorityBList.remove(node)
            return node
        else:
            return None

    def DequeueB(self):
        """Pop off the entry with the highest priority B."""
        if len(self.queue) > 0:
            node = self.priorityBList.pop(0)
            self.queue.remove(node)
            self.priorityAList.remove(node)
            return node
        else:
            return None
