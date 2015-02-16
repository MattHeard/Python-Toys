class DoublePriorityQueue:

    def __init__(self):
        self.count = 0

    def Enqueue(self, val, priorityA, priorityB):
        node = Node(val, priorityA, priorityB)
        self.push(node)

    def DequeueA(self):
        return self.popPriorityA()

    def DequeueB(self):
        return self.popPriorityB()

    def Count(self):
        return self.count

    def Clear(self):
        pass

    def push(self, node):
        if self.Count() is 0:
            self.first = node
            self.topPriorityA = node
            self.topPriorityB = node
            self.count += 1

    def popPriorityA(self):
        pass

    def popPriorityB(self):
        pass

class Node:

    def __init__(self, val, priorityA, priorityB):
        pass
