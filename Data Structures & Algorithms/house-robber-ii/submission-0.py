class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        res1 = self.helper(nums, 0, n-2)
        res2 = self.helper(nums, 1, n-1)
        return max(res1, res2)

    def helper(self, nums: List[int], start: int, end: int) -> int:
        dp = [nums[start], 0]
        for i in range(start+1, end+1):
            dp[(i-start)%2] = max(dp[(i-start-1)%2], nums[i] + dp[(i-start)%2])
        return dp[(end-start)%2]
        