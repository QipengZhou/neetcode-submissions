class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)
        for i in range(1, m+1):
            prev = dp[0]
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    cur = prev + 1
                else:
                    cur = max(dp[j-1], dp[j])
                prev = dp[j]
                dp[j] = cur
        return dp[n]