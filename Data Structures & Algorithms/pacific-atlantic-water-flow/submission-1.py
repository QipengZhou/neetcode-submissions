class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        def bfs(starts):
            queue = list(starts)
            visit = set(starts)
            idx = 0
            while idx < len(queue):
                r, c = queue[idx]
                idx += 1
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit and heights[nr][nc] >= heights[r][c]:
                        queue.append((nr, nc))
                        visit.add((nr, nc))
            return visit
        pacificStarts = set()
        for i in range(rows): pacificStarts.add((i, 0))
        for i in range(cols): pacificStarts.add((0, i))
        canPacific = bfs(pacificStarts)
        atlanticStarts = set()
        for i in range(rows): atlanticStarts.add((i, cols-1))
        for i in range(cols): atlanticStarts.add((rows-1, i))
        canAtlantic = bfs(atlanticStarts)
        ans = [list(i) for i in canPacific if i in canAtlantic]
        return ans
