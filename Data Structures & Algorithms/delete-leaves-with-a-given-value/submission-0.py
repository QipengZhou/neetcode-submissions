# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root: Optional[TreeNode], target) -> Optional[TreeNode]:
            if root is None:
                return None
            left = dfs(root.left, target)
            right = dfs(root.right, target)
            if root.val == target and left is None and right is None:
                return None
            root.left = left
            root.right = right
            return root

        return dfs(root, target)
        