class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 0, x
        while l <= h:
            mid = (l + h) // 2
            t = mid * mid
            if t == x:
                return mid
            elif t > x:
                h = mid - 1
            else:
                l = mid + 1
        return h
        