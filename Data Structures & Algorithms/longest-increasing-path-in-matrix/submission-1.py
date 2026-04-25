from collections import deque

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        outdegrees = [[0] * cols for _ in range(rows)]
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                for (dr, dc) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                        outdegrees[r][c] += 1
                if outdegrees[r][c] == 0:
                    queue.append((r, c))
        height = 0
        while queue:
            height += 1
            for _ in range(len(queue)):
                (r, c) = queue.popleft()
                for (dr, dc) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] < matrix[r][c]:
                        outdegrees[nr][nc] -= 1
                        if outdegrees[nr][nc] == 0:
                            queue.append((nr, nc))
        return height