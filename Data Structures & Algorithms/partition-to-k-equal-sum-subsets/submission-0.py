class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = 0
        for num in nums:
            s += num
        if s % k != 0:
            return False
        n = len(nums)
        target = s // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        t = [0] * k
        def backtrack(i):
            if i == n:
                return True
            match = nums[i]
            for j in range(k):
                if (t[j] + match) <= target:
                    t[j] += match
                    if backtrack(i+1):
                        return True
                    t[j] -= match
                if t[j] == 0:
                    break
            return False
        return backtrack(0)
        