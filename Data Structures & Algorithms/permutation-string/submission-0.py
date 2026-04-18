from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = defaultdict(int)
        for c in s1:
            need[c] += 1
        targetNum = 0
        window = defaultdict(int)
        left, right = 0, 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    targetNum += 1
            while (right - left) >= len(s1):
                if targetNum == len(need):
                    return True
                c = s2[left]
                left += 1
                if c in need:
                    if need[c] == window[c]:
                        targetNum -= 1
                    window[c] -= 1
        return False
        