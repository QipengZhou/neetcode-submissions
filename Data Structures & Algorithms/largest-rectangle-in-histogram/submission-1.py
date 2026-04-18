class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, v in enumerate(heights + [0]):
            start = i
            while stack and stack[-1][1] > v:
                index, height = stack.pop()
                maxArea = max(maxArea, (i - index)*height)
                start = index
            stack.append((start, v))
        return maxArea