# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0

        q= deque()
        q.append(root)

        counter=0

        while q:
            nodesInLevel= len(q)
            for i in range (nodesInLevel) : 
                current = q.popleft() #dequeue

                if current.left is not None: 
                    q.append(current.left)
        
                if current.right is not None: 
                    q.append(current.right)
            
            counter+=1

        return counter
    

    
    

        




    
        