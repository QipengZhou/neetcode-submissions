class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        rows, cols = len(grid), len(grid[0])
        queue = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))
        idx = 0
        while idx < len(queue):
            r, c = queue[idx]
            idx += 1

            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))
