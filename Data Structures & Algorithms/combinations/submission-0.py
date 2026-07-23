class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        t = []
        def dfs(i, j):
            nonlocal t
            if j == k:
                ans.append(t[:])
                return
            if i > n:
                return
            dfs(i+1, j)
            t.append(i)
            dfs(i+1, j+1)
            t.pop()
        dfs(1, 0)
        return ans
        