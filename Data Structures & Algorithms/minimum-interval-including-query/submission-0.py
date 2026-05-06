import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = [-1] * len(queries)
        sorted_queries = sorted([(v, i) for i, v in enumerate(queries)])
        min_heap = []
        i = 0

        for q, idx in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                i += 1
                heapq.heappush(min_heap, (r - l + 1, r))

            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            if min_heap:
                res[idx] = min_heap[0][0]
        return res