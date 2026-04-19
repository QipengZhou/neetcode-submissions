class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        res = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if length == 2 and s[i] == s[j]:
                    dp[i][j] = True
                elif s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                if dp[i][j]:
                    res += 1
        return res