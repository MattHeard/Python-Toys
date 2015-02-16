class DoublePriorityQueue:

    def Enqueue(self, val, priorityA, priorityB):
        node = Node(val, priorityA, priorityB)
        self.push(node)

    def DequeueA(self):
        return self.popPriorityA()

    def DequeueB(self):
        return self.popPriorityB()

    def Count(self):
        return 0

    def Clear(self):
        pass

    def push(self, node):
        pass

    def popPriorityA(self):
        pass

    def popPriorityB(self):
        pass

class Node:

    def __init__(self, val, priorityA, priorityB):
        pass
