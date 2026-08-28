class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0

        cur_max = 0
        max_subarray = float('-inf')

        cur_min = 0
        min_subarray = float('inf')

        for num in nums:
            total += num

            cur_max = max(num, cur_max+num)
            max_subarray = max(max_subarray, cur_max)

            cur_min = min(num, cur_min+num)
            min_subarray = min(min_subarray, cur_min)

        if max_subarray < 0:
            return max_subarray

        return max(max_subarray, total - min_subarray)
        