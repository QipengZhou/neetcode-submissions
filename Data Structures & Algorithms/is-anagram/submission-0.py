from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sChars = defaultdict(int)
        for c in s:
            sChars[c] += 1
        for c in t:
            sChars[c] -= 1
        for _, v in sChars.items():
            if v != 0:
                return False
        return True