from collections import deque

class DoublePriorityQueue:

    def __init__(self):
        self.count = 0
        self.queue = deque()
        self.priorityAList = []
        self.priorityBList = []

    def Enqueue(self, val, priorityA, priorityB):
        node = Node(val, priorityA, priorityB)
        self.push(node)

    def Dequeue(self):
        return self.popQueue()

    def DequeueA(self):
        return self.popPriorityA()

    def DequeueB(self):
        return self.popPriorityB()

    def Count(self):
        return self.count

    def Clear(self):
        pass

    def push(self, node):
        self.queue.append(node)
        if self.Count() is 0:
            self.priorityAList.append(node)
            self.priorityBList.append(node)
        else:
            pos = 0
            isAdded = False
            for curr in self.priorityAList:
                if node.priorityA > curr.priorityA:
                    self.priorityAList.insert(pos, node)
                    isAdded = True
                    break
            if isAdded == False:
                self.priorityAList.append(node)
            isAdded = False
            pos = 0
            for curr in self.priorityBList:
                if node.priorityB > curr.priorityB:
                    self.priorityBList.insert(pos, node)
                    isAdded = True
                    break
            if isAdded == False:
                self.priorityBList.append(node)
        self.count += 1

    def popQueue(self):
        if self.count > 0:
            node = self.queue.popleft()
            self.priorityAList.remove(node)
            self.priorityBList.remove(node)
            self.count -= 1
            return node.asTuple()
        else:
            return None

    def popPriorityA(self):
        pass

    def popPriorityB(self):
        pass

class Node:

    def __init__(self, val, priorityA, priorityB):
        self.val = val
        self.priorityA = priorityA
        self.priorityB = priorityB

    def asTuple(self):
        return (self.val, self.priorityA, self.priorityB)
