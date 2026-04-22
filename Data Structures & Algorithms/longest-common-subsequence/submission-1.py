from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        return self.helper(text1, text2, m, n)

    @lru_cache()
    def helper(self, text1: str, text2: str, i: int, j: int) -> int:
        if i == 0 or j == 0:
            return 0
        if text1[i-1] == text2[j-1]:
            return self.helper(text1, text2, i-1, j-1)+1
        return max(self.helper(text1, text2, i-1, j), self.helper(text1, text2, i, j-1))