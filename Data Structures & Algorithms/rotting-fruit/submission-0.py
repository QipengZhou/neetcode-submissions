class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    grid[i][j] = 0
                    queue.append((i, j))
        t = 0
        idx = 0
        while idx < len(queue):
            r, c = queue[idx]
            idx += 1
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = grid[r][c] - 1
                    queue.append((nr, nc))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
                t = min(t, grid[i][j])
        return -t
        