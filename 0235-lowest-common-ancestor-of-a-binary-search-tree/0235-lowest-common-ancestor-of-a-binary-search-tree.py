# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path1= []
        path2=[]
        
        def searchBST(root, target,path):
            if root is None:
                return None

            path.append(root.val)

            if root.val == target:
                return None

            if target < root.val:
                return searchBST(root.left, target,path)
            else:
                return searchBST(root.right, target,path)

        searchBST(root,p.val,path1)
        searchBST(root,q.val,path2)

        lenA= len(path1)
        lenB= len(path2)
        equal=0

        for i in range(min(lenA, lenB)):
            if path1[i] == path2[i]:
                equal= path1[i]
        
        print(path1)
        print(path2)

        return TreeNode(equal)