# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result =[]
        if root is None:
            return []

        Flip = False
        
        q= deque()
        q.append(root)
        

        while q:
            nodesInLevel = len(q)

            result.append([])

            for i in range(nodesInLevel):
                current = q.popleft()

                if Flip == False: 
                    result[-1].append(current.val)
                else:
                    result[-1].insert(0, current.val) 
                
                if current.left is not None:
                    q.append(current.left)
                    
                if current.right is not None:
                    q.append(current.right)
                
                 
            Flip= not Flip

        return result
                
                    




        