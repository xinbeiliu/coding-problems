# https://leetcode.com/problems/subtree-of-another-tree/

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution():
    def isSubtree(self, s, t):
        if s is None and t is None:
            return True
        if t is None:
            return True
        if s is None and t is not None:
            return False
        return self.isSame(s,t) or self.isSubtree(s.left, t) or self.isSubtree(s.right,t)


    def isSame(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        return s.val == t.val and self.isSame(s.left, t.left) and self.isSame(s.right, t.right)