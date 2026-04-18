class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(arr):
            if len(arr) == len(nums):
                res.append(arr[:])
            t = {v: True for v in arr}
            for num in nums:
                if num in t:
                    continue
                arr.append(num)
                backtrack(arr)
                arr.pop()
        backtrack([])
        return res