class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.currentSize = 0
        self.arr = []

    def push(self, x: int) -> None:
        if self.currentSize < self.maxSize:
            self.currentSize += 1
            self.arr.append(x)
        

    def pop(self) -> int:
        if self.currentSize > 0:
            self.currentSize -= 1
            return self.arr.pop()
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i < self.currentSize:
                self.arr[i] += val
            else:
                break


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
