class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]] * 2
        res = dp[0]
        for i in range(1, len(nums)):
            t = max(nums[i], nums[i] + dp[(i+1)%2])
            dp[i%2] = t
            if res < t:
                res = t
        return res