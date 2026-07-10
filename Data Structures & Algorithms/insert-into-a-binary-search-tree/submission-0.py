# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        parent, cur = root, root
        isLeftChild = False
        while True:
            if cur is None:
                if isLeftChild:
                    parent.left = TreeNode(val)
                else:
                    parent.right = TreeNode(val)
                break
            elif cur.val > val:
                isLeftChild = True
                parent, cur = cur, cur.left
            else:
                isLeftChild = False
                parent, cur = cur, cur.right
        return root
        