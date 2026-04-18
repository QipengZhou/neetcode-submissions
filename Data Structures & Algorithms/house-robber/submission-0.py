class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, n):
            dp[i%2] = max(nums[i] + dp[(i-2)%2], dp[(i-1)%2])
        return dp[(n-1)%2]