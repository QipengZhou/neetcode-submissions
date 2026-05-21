import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in times:
            g[u-1].append((v-1, w))
        min_dist = {i: float('inf') for i in range(n)}
        start_node = k - 1
        min_dist[start_node] = 0

        pq = [(0, start_node)]

        while pq:
            curr_dist, u = heapq.heappop(pq)

            if curr_dist > min_dist[u]:
                continue

            for v, weight in g[u]:
                if curr_dist + weight < min_dist[v]:
                    min_dist[v] = curr_dist + weight
                    heapq.heappush(pq, (min_dist[v], v))

        max_time = max(min_dist.values())

        return -1 if max_time == float('inf') else max_time