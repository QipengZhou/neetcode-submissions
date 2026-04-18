class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [height[0]] * len(height)
        suffix = [height[-1]] * len(height)
        for i in range(1, len(height)):
            prefix[i] = max(prefix[i-1], height[i-1])
        for i in range(len(height)-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i+1])
        res = 0
        for i in range(len(height)):
            res += max(0, min(prefix[i], suffix[i])-height[i])
        return res