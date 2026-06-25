class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res, count = "", 0
        for c in s:
            if c == '[':
                stack.append((res, count))
                res, count = "", 0
            elif c == ']':
                last_res, last_count = stack.pop()
                res = last_res + last_count * res
            elif '0' <= c <= '9':
                count = count * 10 + int(c)
            else:
                res += c

        return res
        