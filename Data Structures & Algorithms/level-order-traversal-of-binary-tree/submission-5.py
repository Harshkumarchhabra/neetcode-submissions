# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #first we initialize queue
        queue=collections.deque([root])
        res=[]
        if not root:
            return []
        
        while queue:
            level=[]
            levlen=len(queue)
            for i in range(levlen):
                node=queue.popleft()#we pop form queue the node 
                level.append(node.val)#we add it into sublist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res