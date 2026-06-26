from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        if self.freq[val] > self.max_freq:
            self.max_freq = self.freq[val]
        self.group[self.freq[val]].append(val)

    def pop(self) -> int:
        t = self.group[self.max_freq].pop()
        self.freq[t] -= 1
        if len(self.group[self.max_freq]) == 0:
            self.max_freq -= 1
        return t


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()