from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(set)
        degree = [0] * n
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            degree[u] += 1
            degree[v] += 1

        queue = deque()
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)

        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(queue)
            remaining_nodes -= leaves_count

            for _ in range(leaves_count):
                leaf = queue.popleft()
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                degree[neighbor] -= 1

                if degree[neighbor] == 1:
                    queue.append(neighbor)
        return list(queue)