# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, h = 1, n+1
        while True:
            mid = (l + h) // 2
            t = guess(mid)
            if t == 0:
                return mid
            elif t < 0:
                h = mid
            else:
                l = mid+1
        