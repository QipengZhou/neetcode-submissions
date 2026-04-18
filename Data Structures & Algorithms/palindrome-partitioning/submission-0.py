class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(start, t):
            if start == len(s):
                res.append(t[:])
                return
            for i in range(start+1, len(s)+1):
                a = s[start:i]
                if a == a[::-1]:
                    t.append(a)
                    dfs(i, t)
                    t.pop()
        dfs(0, [])
        return res