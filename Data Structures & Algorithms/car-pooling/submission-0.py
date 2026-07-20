from collections import defaultdict
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = defaultdict(int)
        for num, start, end in trips:
            changes[start] += num
            changes[end] -= num
        currentPassengers = 0
        for station in sorted(changes.keys()):
            currentPassengers += changes[station]
            if currentPassengers > capacity:
                return False
        return True