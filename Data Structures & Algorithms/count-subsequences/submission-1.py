class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1, n2 = len(s), len(t)
        if n2 > n1:
            return 0
        dp = [[0] * (n2+1) for _ in range(n1+1)]
        for i in range(n1+1):
            dp[i][0] = 1
        for i in range(n1):
            for j in range(n2):
                if j > i:
                    break
                if s[i] == t[j]:
                    dp[i+1][j+1] = (dp[i][j] + dp[i][j+1])
                else:
                    dp[i+1][j+1] = dp[i][j+1]
        return dp[n1][n2]