import heapq

class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        elif len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        lmin, lmax = len(self.minHeap), len(self.maxHeap)
        if (lmin + lmax) % 2 == 0:
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        else:
            if lmin > lmax:
                return self.minHeap[0] * 1.0
            else:
                return (-self.maxHeap[0]) * 1.0
        
        