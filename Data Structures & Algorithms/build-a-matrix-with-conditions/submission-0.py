from collections import defaultdict, deque
from typing import List


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(edges: List[List[int]]) -> List[int]:
            adj = defaultdict(list)
            indegree = [0] * (k + 1)
            for u, v in edges:
                adj[u].append(v)
                indegree[v] += 1

            queue = deque([i for i in range(1, k+1) if indegree[i] == 0])
            order = []

            while queue:
                curr = queue.popleft()
                order.append(curr)
                for nxt in adj[curr]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        queue.append(nxt)
            return order if len(order) == k else []
        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)
        if not row_order or not col_order:
            return []

        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}

        ans = [[0]*k for _ in range(k)]
        for num in range(1, k+1):
            r = row_pos[num]
            c = col_pos[num]
            ans[r][c] = num
        return ans