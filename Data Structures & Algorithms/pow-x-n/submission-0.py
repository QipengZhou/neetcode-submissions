class Solution:
    def fastPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if x == 0:
            return x
        if n % 2 == 0:
            return self.fastPow(x, n // 2) ** 2
        else:
            return x * self.fastPow(x, n // 2) ** 2

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n > 0:
            return self.fastPow(x, n)
        else:
            return 1.0 / self.fastPow(x, -n)