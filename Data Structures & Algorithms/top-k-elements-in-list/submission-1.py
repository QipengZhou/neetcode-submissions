from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        buckets = [[] for _ in range(len(nums)+1)]
        for key, val in mp.items():
            buckets[val].append(key)
        res = []
        for i in range(len(nums), 0, -1):
            if len(buckets[i]) == 0:
                continue
            res.extend(buckets[i])
            k -= len(buckets[i])
            if k <= 0:
                break
        return res
