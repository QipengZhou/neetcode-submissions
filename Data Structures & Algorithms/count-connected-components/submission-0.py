from collections import deque, defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        while len(visited) != n:
            ans += 1
            queue = deque()
            for i in range(n):
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
                    break
            while queue:
                node = queue.popleft()
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        return ans
        