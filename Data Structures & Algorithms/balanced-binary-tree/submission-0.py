# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(root):
            if not root:
                return 0
            ld = dfs(root.left)
            rg = dfs(root.right)
            return 1 + max(ld, rg)
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        ld = dfs(root.left)
        rg = dfs(root.right)
        return left and right and abs(ld - rg) <= 1
        