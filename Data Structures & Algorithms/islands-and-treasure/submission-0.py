class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasures = []
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    treasures.append((i, j))
        for (i, j) in treasures:
            t = [(i, j),]
            visit = set((i,j))
            d = 0
            while len(t) > 0:
                n = len(t)
                d += 1
                for k in range(n):
                    ii, jj = t[k]
                    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ni, nj = ii+dr ,jj+dc
                        if 0 <= ni < rows and 0 <= nj < cols:
                            if (ni, nj) in visit:
                                continue
                            if grid[ni][nj] == -1 or grid[ni][nj] == 0:
                                continue
                            grid[ni][nj] = min(grid[ni][nj], d)
                            visit.add((ni, nj))
                            t.append((ni, nj))
                t = t[n:]       
