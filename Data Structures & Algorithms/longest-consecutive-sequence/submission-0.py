from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        mp = defaultdict(bool)
        for num in nums:
            mp[num] = True
        for num in nums:
            if mp[num-1]:
                continue
            mx = 1
            while mp[num+mx]:
                mx += 1
            if res < mx:
                res = mx
        return res