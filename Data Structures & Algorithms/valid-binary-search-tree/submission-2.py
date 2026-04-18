# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBST(root: Optional[TreeNode], minVal: Optional[int], maxVal: Optional[int]) -> bool:
            if not root:
                return True
            if minVal is not None and root.val <= minVal:
                return False
            if maxVal is not None and root.val >= maxVal:
                return False
            return isBST(root.left, minVal, root.val) and isBST(root.right, root.val, maxVal)
        return isBST(root, None, None)