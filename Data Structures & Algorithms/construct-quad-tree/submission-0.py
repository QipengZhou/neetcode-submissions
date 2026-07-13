"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r1, c1, r2, c2):
            if r1 == r2 and c1 == c2:
                return Node(val=grid[r1][c1], isLeaf=True)
            rowMid = (r1 + r2) // 2
            colMid = (c1 + c2) // 2
            topLeft = dfs(r1, c1, rowMid, colMid)
            topRight = dfs(r1, colMid+1, rowMid, c2)
            bottomLeft = dfs(rowMid+1, c1, r2, colMid)
            bottomRight = dfs(rowMid+1, colMid+1, r2, c2)
            if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return Node(val=topLeft.val, isLeaf=True)
            return Node(val=1, isLeaf=False, topLeft=topLeft, topRight=topRight, bottomLeft=bottomLeft, bottomRight=bottomRight)

        n = len(grid)
        return dfs(0, 0, n-1, n-1)
        