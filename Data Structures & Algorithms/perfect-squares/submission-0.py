class Solution:
    def numSquares(self, n: int) -> int:
        target = [n] * (n+1)
        target[0] = 0
        target[1] = 1
        for i in range(2, n+1):
            for t in range(1, i):
                if t * t > i:
                    break
                target[i] = min(target[i], target[i-t*t]+1)
        return target[n]
        