class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        s = 0
        n = len(nums)
        def backtracking(i):
            nonlocal s, ans
            if i == n:
                ans += s
                return
            backtracking(i+1)

            s ^= nums[i]
            backtracking(i+1)
            s ^= nums[i]
        backtracking(0)
        return ans
        