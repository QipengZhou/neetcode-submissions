# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = 0
        mp = {v: i for i, v in enumerate(inorder)}

        def helper(start, end) -> Optional[TreeNode]:
            nonlocal preIdx

            if start > end:
                return None
            nodeVal = preorder[preIdx]
            idx = mp[nodeVal]
            root = TreeNode(nodeVal)
            preIdx += 1
            left = helper(start, idx-1)
            right = helper(idx+1, end)
            root.left = left
            root.right = right
            return root
        return helper(0, len(inorder)-1)
