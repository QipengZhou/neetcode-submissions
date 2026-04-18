class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        while low <= high:
            p1 = (low + high) // 2
            p2 = (m + n + 1) // 2 - p1
            maxLeft1 = nums1[p1-1] if p1 > 0 else float('-inf')
            minRight1 = nums1[p1] if p1 < m else float('inf')
            maxLeft2 = nums2[p2-1] if p2 > 0 else float('-inf')
            minRight2 = nums2[p2] if p2 < n else float('inf')
            if maxLeft1 <= minRight2 and minRight1 >= maxLeft2:
                if (m + n) % 2 == 1:
                    return max(maxLeft1, maxLeft2)
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            elif maxLeft1 > minRight2:
                high = p1 - 1
            else:
                low = p1 + 1

