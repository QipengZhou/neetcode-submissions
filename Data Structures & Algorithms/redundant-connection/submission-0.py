class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        def find(i):
            if parent[i] == i:
                return i
            return find(parent[i])
        
        def union(u, v):
            pu = find(u)
            pv = find(v)
            if pu == pv:
                return False
            parent[pu] = pv
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]