class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return x
        if n < 0:
            x = 1.0 / x
            n = -n
        res = 1.0
        cur = x
        while n > 0:
            if n % 2 == 1:
                res *= cur
            cur *= cur
            n = n // 2
        return res