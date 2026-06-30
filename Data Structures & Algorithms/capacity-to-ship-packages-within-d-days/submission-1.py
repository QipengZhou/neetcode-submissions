class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        h, l = 0, float('-inf')
        for w in weights:
            h += w
            l = max(l, w)
        while l < h:
            mid = (l + h) // 2
            needDays = 0
            t = 0
            for w in weights:
                if t + w > mid:
                    needDays += 1
                    t = w
                else:
                    t += w
            needDays += 1
            if needDays <= days:
                h = mid
            else:
                l = mid+1
        return l