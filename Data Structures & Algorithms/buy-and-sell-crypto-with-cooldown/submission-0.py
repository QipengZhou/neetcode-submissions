class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        holding = -prices[0]
        sold = 0
        reset = 0
        for i in range(1, len(prices)):
            prev_holding = holding
            holding = max(holding, reset - prices[i])
            reset = max(reset, sold)
            sold = prev_holding + prices[i]
        return max(reset, sold)