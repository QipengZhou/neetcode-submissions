class Solution:
    def simplifyPath(self, path: str) -> str:
        s = [v for v in path.split('/') if v]
        stk = []
        for v in s:
            if v == '.':
                continue
            elif v == '..':
                if stk:
                    stk.pop()
            else:
                stk.append(v)
        return "/" + '/'.join(stk)