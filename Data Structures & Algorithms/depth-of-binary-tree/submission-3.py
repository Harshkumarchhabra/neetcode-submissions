# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def calc(node,count):
            if not node:
                return 0
            left=calc(node.left,count+1)
            right=calc(node.right,count+1)
            return 1+max(left,right)
        return calc(root,1)
        