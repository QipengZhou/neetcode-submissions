class StockSpanner:

    def __init__(self):
        self.stack = []
        self.idx = -1

    def next(self, price: int) -> int:
        self.idx += 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        if self.stack:
            t = self.idx - self.stack[-1][-1]
        else:
            t = self.idx + 1
        self.stack.append((price, self.idx))
        return t
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)