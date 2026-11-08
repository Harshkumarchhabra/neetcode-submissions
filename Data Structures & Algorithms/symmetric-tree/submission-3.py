# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(leftn,rightn):
            if not leftn and not rightn:
                return True
            if not leftn or not rightn:
                return False
            if leftn.val!=rightn.val:
                return False
            return dfs(leftn.left,rightn.right) and dfs(leftn.right,rightn.left)
        return dfs(root.left,root.right)