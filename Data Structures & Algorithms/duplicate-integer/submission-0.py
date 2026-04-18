class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existed = set()
        for num in nums:
            if num in existed:
                return True
            existed.add(num)
        return False
        