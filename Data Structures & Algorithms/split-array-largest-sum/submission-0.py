class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, h = float('-inf'), 0
        for num in nums:
            l = max(l, num)
            h = h + num
        while l <= h:
            mid = (l + h) // 2
            if mid == h:
                break
            t, s = 1, 0
            for num in nums:
                s += num
                if s > mid:
                    s = num
                    t += 1
            if t > k:
                l = mid + 1
            else:
                h = mid
        return h