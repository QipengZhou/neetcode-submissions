class Solution:
    def isValid(self, s: str) -> bool:
        rightParentheses = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c in rightParentheses:
                if len(stack) == 0 or stack[-1] != rightParentheses[c]:
                    return False
                stack = stack[:-1]
            else:
                stack.append(c)
        return len(stack) == 0