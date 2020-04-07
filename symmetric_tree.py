# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):

        if left == None and right == None:
            return True
        elif left != None and right != None:
            return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right,
                                                                                                     right.left)
        return False

# O(n) - time complexity (touch each node in the tree)
# O(h) - space complexity (height of the tree)

    def isSymmetric_iterative(self, root):
        from collections import deque

        if root is None:
            return True

        queue = deque([root])
        queue.append(root)

        while queue:
            left = queue.pop()
            right = queue.pop()

            if left is None and right is None:
                continue
            elif left is None or right is None:
                return False
            elif left.val != right.val:
                return False

            queue.append(left.left)
            queue.append(right.right)

            queue.append(left.right)
            queue.append(right.left)

        return True