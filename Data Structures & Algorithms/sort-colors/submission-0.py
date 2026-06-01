class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, 0
        for num in nums:
            if num == 0:
                r += 1
            elif num == 1:
                w += 1
            else:
                b += 1
        i = 0
        for _ in range(r):
            nums[i] = 0
            i += 1
        for _ in range(w):
            nums[i] = 1
            i += 1
        for _ in range(b):
            nums[i] = 2
            i += 1
        