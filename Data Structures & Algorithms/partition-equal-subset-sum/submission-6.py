class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for num in nums:
            total += num
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        dp = [None] * (target+1)
        for j in range(target+1):
            dp[j] = False
        dp[0] = True
        for i in range(1, n+1):
            for j in range(target, 0, -1):
                dp[j] = dp[j] or (j >= nums[i-1] and dp[j-nums[i-1]])
        return dp[target]