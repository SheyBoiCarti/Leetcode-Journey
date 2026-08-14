# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        #diameter is height of left subtree+ height of right for a given node
        max_diameter=[0]

        def getHeight(root):
            if root is None:
                return 0
            
            left= getHeight(root.left)
            right= getHeight(root.right)
            current_diameter= left+ right

            max_diameter[0]= max(max_diameter[0],current_diameter)

            return 1+ max(left,right)

        getHeight(root)

        return max_diameter[0]
        
    
        
        




        