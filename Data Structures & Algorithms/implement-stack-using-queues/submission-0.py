class MyStack:

    def __init__(self):
        self.que1 = []
        self.que2 = []

    def push(self, x: int) -> None:
        if self.que2:
            self.que2.append(x)
        else:
            self.que1.append(x)

    def pop(self) -> int:
        if self.que1:
            while len(self.que1) > 1:
                self.que2.append(self.que1.pop(0))
            return self.que1.pop(0)
        else:
            while len(self.que2) > 1:
                self.que1.append(self.que2.pop(0))
            return self.que2.pop(0)

    def top(self) -> int:
        if self.que1:
            while len(self.que1) > 1:
                self.que2.append(self.que1.pop(0))
            t = self.que1[0]
            self.que2.append(t)
            return self.que1.pop(0)
        else:
            while len(self.que2) > 1:
                self.que1.append(self.que2.pop(0))
            t = self.que2[0]
            self.que1.append(t)
            return self.que2.pop(0)

    def empty(self) -> bool:
        return len(self.que1) == 0 and len(self.que2) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()