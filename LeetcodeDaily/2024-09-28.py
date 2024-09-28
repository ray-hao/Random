class MyCircularDeque:

    def __init__(self, k: int):
        self.currentSize = 0
        self.maxSize = k
        self.elements = []

    def insertFront(self, value: int) -> bool:
        if self.currentSize < self.maxSize:
            self.currentSize += 1
            self.elements.insert(0, value)
            return True

        return False
        
    def insertLast(self, value: int) -> bool:
        if self.currentSize < self.maxSize:
            self.currentSize += 1
            self.elements.append(value)
            return True

        return False
        

    def deleteFront(self) -> bool:
        if self.currentSize > 0:
            self.currentSize -= 1
            self.elements.pop(0)
            return True

        return False    

    def deleteLast(self) -> bool:
        if self.currentSize > 0:
            self.currentSize -= 1
            self.elements.pop(len(self.elements) - 1)
            return True

        return False 

    def getFront(self) -> int:
        if self.currentSize > 0:
            return self.elements[0]
        return -1

    def getRear(self) -> int:
        if self.currentSize > 0:
            return self.elements[-1]
        return -1

    def isEmpty(self) -> bool:
        return self.currentSize == 0

    def isFull(self) -> bool:
        return self.currentSize == self.maxSize
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
