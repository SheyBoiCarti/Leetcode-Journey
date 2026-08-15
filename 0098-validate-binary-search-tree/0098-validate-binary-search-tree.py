# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):

        result=[]
        def inorder(root):
            if root is None:
                return  True
            
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
        
        inorder(root)

        print(result)

        current=0
        length= len(result)

        while(current+1 < length):
            if result[current] >= result[current+1]: 
                return False
            else:
                current+=1
        
        return True



    