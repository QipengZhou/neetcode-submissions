class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        preMin = prices[0]
        res = 0
        for v in prices[1:]:
            res = max(res, v - preMin)
            if preMin > v:
                preMin = v
        return res
        