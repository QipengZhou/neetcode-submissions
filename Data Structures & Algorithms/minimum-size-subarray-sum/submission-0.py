class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans, t = 0, 0
        l, r = 0, 0
        for r, v in enumerate(nums):
            t += v
            if t >= target:
                while l < r and (t - nums[l]) >= target:
                    t -= nums[l]
                    l += 1
                if ans != 0:
                    ans = min(ans, r - l + 1)
                else:
                    ans = r - l + 1
        return ans