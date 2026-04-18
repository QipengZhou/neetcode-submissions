class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visit = set()
        row, col = len(grid), len(grid[0])
        def dfs(r, c):
            if (r, c) in visit:
                return
            visit.add((r, c))
            for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                newr, newc = r + dr, c + dc
                if 0 <= newr < row and 0 <= newc < col and grid[newr][newc] == '1':
                    if (newr, newc) not in visit:
                        dfs(newr, newc)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i, j) not in visit:
                    res += 1
                    dfs(i, j)
        return res