class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1, n2 = len(s), len(t)
        if n2 > n1:
            return 0
        dp = [0] * (n2+1)
        dp[0] = 1
        prev = 0
        for i in range(n1):
            for j in range(min(n2-1, i), -1, -1):
                if s[i] == t[j]:
                    dp[j+1] += dp[j]
        return dp[n2]