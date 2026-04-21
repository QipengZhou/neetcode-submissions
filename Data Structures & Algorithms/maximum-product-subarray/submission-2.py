class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        preMin, preMax = nums[0], nums[0]
        res = preMax
        for i in range(1, len(nums)):
            preMin, preMax = min(nums[i], nums[i] * preMax, nums[i] * preMin), max(nums[i], nums[i] * preMax, nums[i] * preMin)
            if preMax > res:
                res = preMax
        return res