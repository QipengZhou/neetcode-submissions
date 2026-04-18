class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[low]:
                if nums[low] <= target < nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high-1]:
                    low = mid + 1
                else:
                    high = mid
        return -1