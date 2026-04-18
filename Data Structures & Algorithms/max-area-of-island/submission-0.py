class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visit = set()
        row, col = len(grid), len(grid[0])
        def dfs(r, c):
            if (r, c) in visit:
                return 0
            visit.add((r, c))
            t = 1
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                newr, newc = r + dr, c + dc
                if 0 <= newr < row and 0 <= newc < col and grid[newr][newc] == 1:
                    t += dfs(newr, newc)
            return t
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i, j) not in visit:
                    res = max(res, dfs(i, j))
        return res