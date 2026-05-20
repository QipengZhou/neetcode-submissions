class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2147483648, 2147483647
        sign = -1 if x < 0 else 1
        x = abs(x)

        res = 0
        while x != 0:
            pop = x % 10
            x //= 10

            res = res * 10 + pop

        res *= sign

        if res < INT_MIN or res > INT_MAX:
            return 0

        return res