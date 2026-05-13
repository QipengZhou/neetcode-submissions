from typing import List
from collections import Counter

class CountSquares:
    def __init__(self):
        self.pts = []
        self.pts_count = Counter()

    def add(self, point: List[int]) -> None:
        p = tuple(point)
        self.pts_count[p] += 1
        self.pts.append(p)

    def count(self, point: List[int]) -> int:
        qx, qy = point
        res = 0

        for (px, py), count in self.pts_count.items():
            if abs(qx - px) > 0 and abs(qx - px) == abs(qy - py):
                if (qx, py) in self.pts_count and (px, qy) in self.pts_count:
                    res += count * self.pts_count[(qx, py)] * self.pts_count[(px, qy)]
        return res