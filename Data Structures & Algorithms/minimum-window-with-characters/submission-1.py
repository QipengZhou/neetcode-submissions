from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        for c in t:
            need[c] += 1
        window = defaultdict(int)
        valid = 0
        left, right = 0, 0
        ml, mr = 0, 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1
            if c in need and window[c] == need[c]:
                valid += 1
            while (right - left) >= len(t):
                if valid == len(need):
                    if (mr - ml) == 0 or (right - left) < (mr - ml):
                        ml, mr = left, right
                c = s[left]
                if c in need and need[c] == window[c]:
                    break
                left += 1
                window[c] -= 1
        return s[ml:mr]
            