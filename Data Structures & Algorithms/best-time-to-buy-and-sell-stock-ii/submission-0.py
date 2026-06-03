class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, -prices[0]], [0, 0]]
        n = len(prices)
        for i in range(1, n):
            cur = i % 2
            pre = (i + 1) % 2
            dp[cur][0] = max(dp[pre][0], dp[pre][1] + prices[i])
            dp[cur][1] = max(dp[pre][1], dp[pre][0] - prices[i])
        return max(dp[(n+1)%2][0], dp[(n+1)%2][1])