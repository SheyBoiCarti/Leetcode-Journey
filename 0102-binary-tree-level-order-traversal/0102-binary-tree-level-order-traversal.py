# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
            
        result= []
        q=deque()
        level=0

        q.append(root)

        while q :
            numberOfNodes = len(q)
            result.append([])

            for i in range(numberOfNodes):
                current = q.popleft()
                result[-1].append(current.val)

                if current.left is not None:
                    q.append(current.left)
                if current.right is not None:
                    q.append(current.right)
        
        return result
                




        