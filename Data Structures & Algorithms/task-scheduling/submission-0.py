import heapq
from collections import deque, Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        c = Counter(tasks)
        maxHeap = [-v for v in c.values()]
        heapq.heapify(maxHeap)
        que = deque()
        while maxHeap or que:
            time += 1
            if maxHeap:
                t = heapq.heappop(maxHeap)
                t += 1
                if t != 0:
                    que.append((t, time + n))
            if que and que[0][1] <= time:
                heapq.heappush(maxHeap, que.popleft()[0])
        return time
