from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.count -= 1
            return True
        return False


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        new_edges = []
        for i, (u, v, w) in enumerate(edges):
            new_edges.append((u, v, w, i))
        new_edges.sort(key=lambda x: x[2])

        def get_mst_weight(skip_edge_idx=-1, force_edge_idx=-1):
            uf = UnionFind(n)
            total_weight = 0
            if force_edge_idx != -1:
                u, v, w = edges[force_edge_idx]
                uf.union(u, v)
                total_weight += w

            for u, v, w, original_idx in new_edges:
                if original_idx == skip_edge_idx:
                    continue
                if uf.union(u, v):
                    total_weight += w

            return total_weight if uf.count == 1 else float('inf')

        origin_mst_weight = get_mst_weight()
        critical = []
        pseudo_critical = []

        for i in range(len(edges)):
            if get_mst_weight(skip_edge_idx=i) > origin_mst_weight:
                critical.append(i)
            elif get_mst_weight(force_edge_idx=i) == origin_mst_weight:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]
        