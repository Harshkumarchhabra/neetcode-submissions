# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def mirror(leftn,rightn):
            if not root:
                return True
            if not leftn and not rightn:
                return True
            if not leftn or not rightn :
                return False
            if leftn.val!=rightn.val:
                return False
            return mirror(leftn.left,rightn.right) and mirror(leftn.right,rightn.left)
        return mirror(root.left,root.right)