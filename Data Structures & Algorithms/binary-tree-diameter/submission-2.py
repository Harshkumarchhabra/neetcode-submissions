# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0
        
        def diam(node):
            if not node:
                return 0
            leftn=diam(node.left)
            rightn=diam(node.right)
            self.res=max(self.res,leftn+rightn)
            return 1+max(leftn,rightn)
        diam(root)
        return self.res