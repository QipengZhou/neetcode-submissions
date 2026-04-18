class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        i = len(temperatures) - 1
        stack = []
        while i >= 0:
            while len(stack) > 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack = stack[:-1]
            if len(stack) > 0:
                res[i] = stack[-1] - i
            stack.append(i)
            i -= 1
        return res