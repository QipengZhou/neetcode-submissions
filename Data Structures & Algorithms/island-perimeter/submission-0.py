class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        r, c = len(grid), len(grid[0])
        vis = [[False] * c for _ in range(r)]
        queue = []
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    queue.append((i, j))
        while queue:
            (i, j) = queue[0]
            queue = queue[1:]
            if vis[i][j]:
                continue
            vis[i][j] = True
            for (dr, dc) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = i+dr, j+dc
                if nr < 0 or nr >= r or nc < 0 or nc >= c or grid[nr][nc] == 0:
                    ans += 1
                elif grid[nr][nc] == 1:
                    if not vis[nr][nc]:
                        queue.append((nr, nc))
        return ans
        