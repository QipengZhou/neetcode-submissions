# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def maxGain(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            leftGain = max(maxGain(root.left), 0)
            rightGain = max(maxGain(root.right), 0)
            current = root.val + leftGain + rightGain
            if current > self.res:
                self.res = current
            return root.val + max(leftGain, rightGain)
        maxGain(root)
        return self.res