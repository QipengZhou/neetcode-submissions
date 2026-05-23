from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattanDist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        vis = set()
        min_heap = [(0, 0)]
        ans = 0
        while len(vis) < len(points):
            d, u = heapq.heappop(min_heap)
            if u in vis:
                continue
            ans += d
            vis.add(u)
            for v in range(len(points)):
                if v in vis:
                    continue
                heapq.heappush(min_heap, (manhattanDist(points[u], points[v]), v))
        return ans