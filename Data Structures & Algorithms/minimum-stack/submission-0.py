import heapq

class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or self.minStack[-1] >= val:
            self.minStack.append(val)

    def pop(self) -> None:
        a = self.stack[-1]
        self.stack = self.stack[:-1]
        if self.minStack[-1] == a:
            self.minStack = self.minStack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
