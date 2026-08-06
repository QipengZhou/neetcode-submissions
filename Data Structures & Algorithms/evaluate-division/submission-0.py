from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for i, equation in enumerate(equations):
            for j in equation:
                if j not in graph:
                    graph[j] = defaultdict(float)
            graph[equation[0]][equation[1]] = values[i]
            graph[equation[1]][equation[0]] = 1.0 / values[i]
        def dfs(i: str, j: str, visited: set) -> float:
            if i not in graph or j not in graph:
                return -1.0
            if i == j:
                return 1.0
            visited.add(i)
            for neighbor, weight in graph[i].items():
                if neighbor not in visited:
                    res = dfs(neighbor, j, visited)
                    if res != -1.0:
                        return weight * res
            return -1.0

        ans = [-1.0] * len(queries)
        for i, query in enumerate(queries):
            ans[i] = dfs(query[0], query[1], set())

        return ans