from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        mp = defaultdict(int)
        mp[0] = 1
        t = 0
        for num in nums:
            t += num
            res += mp[t - k]
            mp[t] += 1
        return res
        