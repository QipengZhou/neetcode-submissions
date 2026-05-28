from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pre = -1
        ans = 0
        for num in nums:
            if num != val:
                pre += 1
                nums[pre] = num
                ans += 1
        return ans