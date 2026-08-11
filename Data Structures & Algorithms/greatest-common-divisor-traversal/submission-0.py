from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        if 1 in nums:
            return False

        max_val = max(nums)
        uf = UnionFind(max_val + 1)

        for num in nums:
            temp = num
            d = 2
            while d * d <= temp:
                if temp % d == 0:
                    uf.union(num, d)
                    while temp % d == 0:
                        temp //= d
                d += 1
            if temp > 1:
                uf.union(num, temp)

        first_root = uf.find(nums[0])
        for i in range(1, n):
            if uf.find(nums[i]) != first_root:
                return False
        return True