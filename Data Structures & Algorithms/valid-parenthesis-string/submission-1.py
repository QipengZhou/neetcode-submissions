class Solution:
    def checkValidString(self, s: str) -> bool:
        minL, maxL = 0, 0
        for c in s:
            if c == '(':
                maxL += 1
                minL += 1
            elif c == '*':
                maxL += 1
                minL -= 1
            else:
                maxL -= 1
                minL -= 1
            if maxL < 0:
                return False
            if minL < 0:
                minL = 0
        return minL == 0