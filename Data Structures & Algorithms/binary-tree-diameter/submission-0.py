# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0# making res instance of upper fn , so it can also be called by inner fn

        #calculating the height
        def dfs(node):
            if not node:
                return 0
            
            left=dfs(node.left)
            right=dfs(node.right)
            self.res=max(self.res,left+right) #diameter
            return 1+ max(left,right)

        dfs(root)
        return self.res
