class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0
        n = len(s)
        for i in range(n):
            l, r = i-1, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if (r - l - 1) > resLen:
                resLen = r - l - 1
                res = s[l+1:r]
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if (r - l - 1) > resLen:
                resLen = r - l - 1
                res = s[l+1:r]
        return res