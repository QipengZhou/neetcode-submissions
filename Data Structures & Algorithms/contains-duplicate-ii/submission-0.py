class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        t = dict()
        for i, v in enumerate(nums):
            if v in t and i - t[v] <= k:
                return True
            else:
                t[v] = i
        return False