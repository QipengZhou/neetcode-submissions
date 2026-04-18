class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix = [1] * (N + 1)
        suffix = [1] * (N + 1)
        res = [0] * N
        for i in range(N):
            prefix[i+1] = prefix[i]*nums[i]
        for i in range(N-1, -1, -1):
            suffix[i] = suffix[i+1]*nums[i]
        for i in range(N):
            res[i] = prefix[i] * suffix[i+1]
        return res
