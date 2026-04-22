from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.helper(m-1, n-1)

    @lru_cache
    def helper(self, i: int, j: int) -> int:
        if i == 0 or j == 0:
            return 1
        return self.helper(i, j-1) + self.helper(i-1, j)