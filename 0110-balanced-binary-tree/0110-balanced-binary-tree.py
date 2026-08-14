from collections import deque

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        if root is None:
            return True

        q = deque()
        q.append(root)

        def height(root):
            if root is None:
                return 0

            left = height(root.left)
            right = height(root.right)

            return 1 + max(left, right)

        while q:
            popped = q.popleft()

            heightleft = height(popped.left)
            heightright = height(popped.right)

            if abs(heightleft - heightright) > 1:
                return False

            if popped.left is not None:
                q.append(popped.left)

            if popped.right is not None:
                q.append(popped.right)

        return True