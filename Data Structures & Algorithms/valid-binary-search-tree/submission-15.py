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
        def valid(node,leftN,rightN):
            if not node:
                return True
            if not (leftN<node.val<rightN):
                return False
            return valid(node.left,leftN,node.val) and valid(node.right,node.val,rightN)
        return valid(root,float('-inf'),float('inf'))
        