class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftMin, rightMin = [0] * len(heights), [0] * len(heights)
        leftStack = []
        for i, v in enumerate(heights):
            while len(leftStack) > 0 and heights[leftStack[-1]] >= v:
                leftStack = leftStack[:-1]
            if len(leftStack)  == 0:
                leftMin[i] = 0
            else:
                leftMin[i] = leftStack[-1] + 1
            leftStack.append(i)
        rightStack = []
        i = len(heights) - 1
        while i >= 0:
            v = heights[i]
            while len(rightStack) > 0 and heights[rightStack[-1]] >= v:
                rightStack = rightStack[:-1]
            if len(rightStack) == 0:
                rightMin[i] = len(heights)
            else:
                rightMin[i] = rightStack[-1]
            rightStack.append(i)
            i -= 1
        res = 0
        for i, v in enumerate(heights):
            res = max(res, v * (rightMin[i] - leftMin[i]))
        return res