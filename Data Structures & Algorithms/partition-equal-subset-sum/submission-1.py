class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for num in nums:
            total += num
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        dp = [[None] * (target+1) for _ in range(n+1)]
        return self.helper(nums, dp, n, target)

    def helper(self, nums: List[int], dp: List[List[int]], i: int, j: int) -> bool:
        if dp[i][j] is None:
            if j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = False
            else:
                dp[i][j] = self.helper(nums, dp, i-1, j)
                if not dp[i][j] and j >= nums[i-1]:
                    dp[i][j] = self.helper(nums, dp, i-1, j-nums[i-1])
        return dp[i][j]