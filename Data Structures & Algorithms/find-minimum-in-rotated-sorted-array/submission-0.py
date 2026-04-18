class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float("inf")
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] >= nums[low]:
                res = min(res, nums[low])
                low = mid + 1
            else:
                res = min(res, nums[mid])
                high = mid
        return res