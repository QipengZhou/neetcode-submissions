from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadset = set(deadends)
        if "0000" in deadset:
            return -1
        queue = deque(["0000"])
        visited = set(["0000"])
        step = 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == target:
                    return step
                for i in range(4):
                    digit = int(curr[i])
                    for dx in (-1, 1):
                        new_digit = (digit + dx) % 10
                        next_state = curr[:i] + str(new_digit) + curr[i+1:]
                        if next_state not in deadset and next_state not in visited:
                            visited.add(next_state)
                            queue.append(next_state)
            step += 1
        return -1