from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        mx = 0
        mp = defaultdict(int)
        left, right = 0, 0
        while right < len(s):
            t = s[right]
            right += 1
            mp[t] += 1
            mx = max(mx, mp[t])
            while (right - left - mx) > k:
                mp[s[left]] -= 1
                left += 1
            res = max(res, right - left)
        return res