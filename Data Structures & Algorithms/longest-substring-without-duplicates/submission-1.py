from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left, right = 0, 0
        mp = defaultdict(int)
        while right < len(s):
            c = s[right]
            right += 1
            mp[c] += 1
            while mp[c] > 1:
                mp[s[left]] -= 1
                left += 1
            res = max(res, right - left)
        return res
        