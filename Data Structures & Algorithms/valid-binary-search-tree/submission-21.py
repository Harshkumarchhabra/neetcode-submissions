# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(minval,node,maxval):
            if not node:
                return True
            if not minval and not maxval:
                return True
            if not (minval<node.val<maxval):
                return False
            return dfs(minval,node.left,node.val) and dfs(node.val,node.right,maxval)
        return dfs(float('-inf'),root,float('inf'))