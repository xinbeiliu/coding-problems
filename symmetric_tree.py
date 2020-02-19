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