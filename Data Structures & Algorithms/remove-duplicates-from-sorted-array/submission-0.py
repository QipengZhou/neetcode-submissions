class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        preIdx = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[preIdx]:
                continue
            preIdx += 1
            nums[preIdx] = nums[i]
        return preIdx + 1
        