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
        def dfs(minv,node,maxv):
            if not node:
                return True

            if not (minv<node.val<maxv):
                return False
            return dfs(minv,node.left,node.val) and dfs(node.val,node.right,maxv)
        return dfs(float('-inf'),root,float('inf'))