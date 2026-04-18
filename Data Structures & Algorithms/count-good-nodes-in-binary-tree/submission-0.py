# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: Tree, maxVal: int) -> int:
            if not root:
                return 0
            mx = maxVal
            res = 0
            if root.val >= mx:
                res += 1
                mx = root.val
            res += dfs(root.left, mx)
            res += dfs(root.right, mx)
            return res
        return dfs(root, -200)