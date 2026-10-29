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
        
        def mirror(node,leftN,rightN):
            # if not node:
            #     return True
            if not leftN and not rightN:
                return True
            if not leftN or not rightN:
                return False
            if leftN.val!=rightN.val:
                return False
            return mirror(node,leftN.left,rightN.right) and mirror(node,leftN.right,rightN.left)
        return mirror(root,root.left,root.right)