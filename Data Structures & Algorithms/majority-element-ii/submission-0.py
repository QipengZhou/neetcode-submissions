class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                count1 = 1
                cand1 = num
            elif count2 == 0:
                count2 = 1
                cand2 = num
            else:
                count1 -= 1
                count2 -= 1

        res = []
        threshold = len(nums) // 3

        actual_count1 = nums.count(cand1) if cand1 is not None else 0
        actual_count2 = nums.count(cand2) if cand2 is not None else 0

        if actual_count1 > threshold:
            res.append(cand1)
        if actual_count2 > threshold and cand2 != cand1:
            res.append(cand2)

        return res