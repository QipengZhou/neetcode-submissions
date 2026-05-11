class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        ans = [0] * n
        t = 1
        for i in range(n):
            a = digits[n-1-i] + t
            if a > 9:
                t, a = divmod(a, 10)
            else:
                t = 0
            ans[i] = a
        if t > 0:
            ans.append(t)
        ans.reverse()
        return ans