from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(set)
        for (a, b) in trust:
            graph[a].add(b)
        if len(graph) != n-1:
            return -1
        pre_trust = (set(range(1, n+1)).difference(set(graph.keys()))).pop()
        for k in graph:
            if pre_trust not in graph[k]:
                return -1
        return pre_trust
        