class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = 0
        for num in nums:
            total += num
        if (total + target) % 2 == 1 or total < target:
            return 0

        return self.subsetSum(nums, (total + target) // 2)

    def subsetSum(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] += dp[j-num]
        return dp[target]