import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for point in points:
            d = point[0] ** 2 + point[1] ** 2
            heapq.heappush(pq, (-d, point))
        while len(pq) > k:
            heapq.heappop(pq)
        return [v[1] for v in pq]
