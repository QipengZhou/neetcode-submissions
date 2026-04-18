import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            t = 0
            for pile in piles:
                t += math.ceil(pile / mid)
            if t <= h:
                if low == high:
                    break
                high = mid
            elif t > h:
                low = mid + 1
        return low