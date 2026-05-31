class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        tmp = [0] * len(nums)
        def mergeSort(i: int, j: int):
            if i >= j:
                return
            mid = (i + j) // 2
            mergeSort(i, mid)
            mergeSort(mid + 1, j)
            k1 = i
            k2 = mid + 1
            cur = i
            while k1 <= mid and k2 <= j:
                if nums[k1] <= nums[k2]:
                    tmp[cur] = nums[k1]
                    k1 += 1
                else:
                    tmp[cur] = nums[k2]
                    k2 += 1
                cur += 1
            while k1 <= mid:
                tmp[cur] = nums[k1]
                k1 += 1
                cur += 1
            while k2 <= j:
                tmp[cur] = nums[k2]
                k2 += 1
                cur += 1
            for idx in range(i, j+1):
                nums[idx] = tmp[idx]
        mergeSort(0, len(nums)-1)
        return nums
        