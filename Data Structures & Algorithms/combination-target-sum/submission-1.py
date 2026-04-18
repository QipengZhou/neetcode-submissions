class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, v, arr):
            if v == target:
                res.append(arr[:])
                return
            for j in range(i, len(nums)):
                new_v = v + nums[j]
                if new_v > target:
                    break
                arr.append(nums[j])
                dfs(j, new_v, arr)
                arr.pop()
        dfs(0, 0, [])
        return res