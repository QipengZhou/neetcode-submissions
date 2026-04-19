class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        res = s[0]
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if length == 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
                if dp[i][j] and length > len(res):
                    res = s[i:(j+1)]
        return res