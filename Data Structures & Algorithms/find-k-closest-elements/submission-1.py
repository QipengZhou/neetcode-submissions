class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        l, h = 0, len(arr)
        while l < h:
            mid = (l + h) // 2
            if mid == l:
                break
            if arr[mid] > x:
                h = mid
            else:
                l = mid
        lt, rt = l, l+1
        for _ in range(k):
            if lt < 0:
                rt += 1
            elif rt >= len(arr):
                lt -= 1
            elif x - arr[lt] <= arr[rt] - x:
                lt -= 1
            else:
                rt += 1
        return arr[lt+1:rt]