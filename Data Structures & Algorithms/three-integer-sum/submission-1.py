class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        N = len(nums)
        i = 0
        while i < len(nums)-2:
            while 0 < i < N and nums[i] == nums[i-1]:
                i += 1
            if i == N:
                break
            target = -nums[i]
            l, r = i+1, N-1
            li = i
            while li < l < r < N:
                t = nums[l] + nums[r]
                if t == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < N and nums[l] == nums[l-1]:
                        l += 1
                elif t > target:
                    r -= 1
                else:
                    l += 1
            i += 1
        return res
        