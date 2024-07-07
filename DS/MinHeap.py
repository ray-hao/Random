import math

class MinHeap:
    
    def __init__(self):
        self.nodes = []

    # insert at the next available position, which will be a leaf node, and fix-up
    # From a parent at index i, its left child will be at (2 * i) + 1, and its right child will be at (2 * i) + 2
    # From a child at index n, it's at index floor((n - 1) / 2)
    def insert(self, key, value):
        self.nodes.append((key, value))
        currentIndex = len(self.nodes) - 1
        while (currentIndex > 0):
            currentKey = self.nodes[currentIndex][0]
            parentIndex = math.floor((currentIndex - 1) / 2)
            parentKey = self.nodes[parentIndex][0]
            if currentKey > parentKey:
                break
            else:
                (self.nodes[currentIndex], self.nodes[parentIndex]) = (self.nodes[parentIndex], self.nodes[currentIndex])
                currentIndex = parentIndex
              
    # we want to delete the root and return it, but if we delete first then we'll need to rebalance 
    # the entire tree, since many holes will be made everywhere. Instead, swap root with last node to maintain balance property.
    def delete(self):
        if len(self.nodes) == 0:
            return "ERROR: EMPTY HEAP"
        (self.nodes[0], self.nodes[-1]) = (self.nodes[-1], self.nodes[0])
        retval = self.nodes.pop(len(self.nodes) - 1)
        # at this point, some large key value is at the root, we need to fix down.
        currentIndex = 0
        while (currentIndex < len(self.nodes)):
            currentKey = self.nodes[currentIndex][0]
            leftIndex = (2 * currentIndex) + 1
            rightIndex = (2 * currentIndex) + 2
            # this should be float('inf') but im too lazy
            leftKey = 9999999999999
            rightKey = 9999999999999
            if (leftIndex < len(self.nodes)):
                leftKey = self.nodes[leftIndex][0]
            if (rightIndex < len(self.nodes)):
                rightKey = self.nodes[rightIndex][0]
            if currentKey <= leftKey and currentKey <= rightKey:
                break
            if leftKey <= rightKey:
                (self.nodes[currentIndex], self.nodes[leftIndex]) = (self.nodes[leftIndex], self.nodes[currentIndex])
                currentIndex = leftIndex
            elif rightKey <= leftKey:
                (self.nodes[currentIndex], self.nodes[rightIndex]) = (self.nodes[rightIndex], self.nodes[currentIndex])
                currentIndex = rightIndex
        return retval
    
    def getMin(self):
        if len(self.nodes) == 0:
            return "ERROR: EMPTY HEAP"
        return self.nodes[0]

myHeap = MinHeap()
myHeap.insert(3, "3")
myHeap.insert(1, "1")
print(myHeap.getMin())  # Expected Output: (1, "1")
myHeap.insert(6, "6")
myHeap.insert(0, "0")
print(myHeap.getMin())  # Expected Output: (0, "0")
print(myHeap.delete())  # Expected Output: (0, "0")
print(myHeap.getMin())  # Expected Output: (1, "1")
myHeap.insert(2, "2")
print(myHeap.delete())  # Expected Output: (1, "1")
print(myHeap.getMin())  # Expected Output: (2, "2")
