import heapq
from collections import defaultdict

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        hp = []
        mp = defaultdict(int)
        res = []
        left, right = 0, 0
        while right < len(nums):
            t = -nums[right]
            heapq.heappush(hp, -nums[right])
            mp[t] += 1
            right += 1
            if (right - left) == k:
                res.append(-hp[0])
                mp[-nums[left]] -= 1
                if mp[-nums[left]] == 0:
                    del mp[-nums[left]]
                left += 1
                while len(hp) > 0 and hp[0] not in mp:
                    heapq.heappop(hp)
        return res