class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        if n2 > n1:
            n2, n1 = n1, n2
            word1, word2 = word2, word1
        dp = list(range(n2+1))
        for i in range(n1):
            prev = dp[0]
            dp[0] = i + 1
            for j in range(n2):
                tmp = dp[j+1]
                if word1[i] == word2[j]:
                    dp[j+1] = prev
                else:
                    dp[j+1] = 1 + min(dp[j+1], dp[j], prev)
                prev = tmp
        return dp[n2]