import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-v for v in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            x -= y
            if x == 0:
                continue
            heapq.heappush(heap, x)
        if len(heap) > 0:
            return -heap[0]
        return 0