from typing import List
from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: List[int]) -> bool:
        n = len(piles)
        suffix_sum = [0] * (n+1)
        for i in range(n-1, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + piles[i]

        @lru_cache(None)
        def dp(i: int, M: int) -> int:
            if i + 2 * M >= n:
                return suffix_sum[i]
            max_stones = 0
            for X in range(1, 2*M + 1):
                current = suffix_sum[i] - dp(i+X, max(M, X))
                max_stones = max(max_stones, current)
            return max_stones
        return dp(0, 1)
        