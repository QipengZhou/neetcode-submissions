class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {
                "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900,
                "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
        }
        res = 0
        i, n = 0, len(s)
        while i < n:
            j = i + 2
            if j <= n and mp.get(s[i:j], 0) > 0:
                res += mp[s[i:j]]
                i = j
            else:
                res += mp[s[i]]
                i += 1
        return res
        