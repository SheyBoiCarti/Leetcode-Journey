# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def rightSideView(self, root):
        result = []

        if root is None:
            return []

        q = deque()
        q.append(root)

        while q:
            numberOfNodesInLevel = len(q)

            for i in range(numberOfNodesInLevel):
                current = q.popleft()

                if current.left is not None:
                    q.append(current.left)

                if current.right is not None:
                    q.append(current.right)

                if i == numberOfNodesInLevel - 1:
                    result.append(current.val)

        return result