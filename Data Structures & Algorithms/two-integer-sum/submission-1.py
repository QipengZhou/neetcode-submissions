class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIdx = dict()
        for i, v in enumerate(nums):
            diff = target - v
            if diff in numIdx:
                return [numIdx[diff], i]
            if v not in numIdx:
                numIdx[v] = i
