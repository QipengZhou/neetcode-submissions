class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d = [0] * 1001
        for v in hand:
            d[v] += 1
        for i, v in enumerate(d):
            if v < 0:
                return False
            if v > 0:
                if (i + groupSize) > len(d):
                    return False
                for j in range(i+1, i+groupSize):
                    d[j] -= v
        return True