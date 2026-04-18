class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights)-1
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            if area > res:
                res = area
            if heights[l] <= heights[r]:
                t = heights[l]
                l += 1
                while l < r and heights[l] <= t:
                    l += 1
            else:
                t = heights[r]
                r -= 1
                while l < r and heights[r] <= t:
                    r -= 1
        return res
        