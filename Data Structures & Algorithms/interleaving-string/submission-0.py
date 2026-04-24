class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if (n1 + n2) != n3:
            return False
        dp = [[None] * (n2 + 1) for _ in range(n1+1)]
        dp[0][0] = True
        for i in range(n1):
            dp[i+1][0] = (s1[i] == s3[i] and dp[i][0])
        for j in range(n2):
            dp[0][j+1] = (s2[j] == s3[j] and dp[0][j])
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                dp[i][j] = (s3[i+j-1] == s1[i-1] and dp[i-1][j]) or (s3[i+j-1] == s2[j-1] and dp[i][j-1])
        return dp[n1][n2]