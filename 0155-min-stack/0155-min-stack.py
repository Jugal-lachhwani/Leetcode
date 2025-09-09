class MinStack:
    
    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        self.s.append(val)

    def pop(self) -> None:
        self.s.pop(len(self.s)-1)

    def top(self) -> int:
        if self.s:
            return self.s[-1]

    def getMin(self) -> int:
        if self.s:
            return min(self.s)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()