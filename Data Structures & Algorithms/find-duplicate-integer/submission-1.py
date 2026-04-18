class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for v in nums:
            t = nums[abs(v)-1]*(-1)
            if t > 0:
                return abs(v)
            nums[abs(v)-1] = t