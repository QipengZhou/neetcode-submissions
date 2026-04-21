class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for num in nums:
            total += num
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        dp = [[None] * (target+1) for _ in range(2)]
        for j in range(target+1):
            dp[0][j] = False
        for i in range(2):
            dp[i][0] = True
        for i in range(1, n+1):
            for j in range(1, target+1):
                dp[i%2][j] = dp[(i+1)%2][j] or (j >= nums[i-1] and dp[(i+1)%2][j-nums[i-1]])
        return dp[n%2][target]