# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]):
            if root is None:
                return (0, 0)
            left_not_rob, left_rob = dfs(root.left)
            right_not_rob, right_rob = dfs(root.right)
            rob_this = root.val + left_not_rob + right_not_rob
            not_rob_this = max(left_not_rob, left_rob) + max(right_not_rob, right_rob)
            return (not_rob_this, rob_this)
        return max(dfs(root))
        