class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [2, 1]
        for i in range(3, n+1):
            dp[i%2] = dp[0] + dp[1]
        return dp[n%2]