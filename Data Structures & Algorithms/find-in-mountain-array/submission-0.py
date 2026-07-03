class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l, h = 0, n - 1
        peak = 0
        while l < h:
            mid = (l + h) // 2
            if mountainArr.get(mid) < mountainArr.get(mid+1):
                l = mid+1
            else:
                h = mid
        peak = l
        l, h = 0, peak
        while l <= h:
            mid = (l + h) // 2
            midVal = mountainArr.get(mid)
            if midVal == target:
                return mid
            elif midVal < target:
                l = mid + 1
            else:
                h = mid - 1
        l, h = peak + 1, n - 1
        while l <= h:
            mid = (l + h) // 2
            midVal = mountainArr.get(mid)
            if midVal == target:
                return mid
            elif midVal > target:
                l = mid + 1
            else:
                h = mid - 1
        return -1