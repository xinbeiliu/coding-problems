# Given a non-empty binary search tree and a target value, find the value in the BST
# that is closest to the target.

# Example:
#
# Input: root = [4,2,5,1,3], target = 3.714286
#
#     4
#    / \
#   2   5
#  / \
# 1   3
#
# Output: 4
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    def closet_value(root, target):
        cur = root
        v = root.val

        while root != None:
            if abs(cur.val - target) < abs(v - target):
                v = cur.val
            if target < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return v

    def closet_value_binary_search(root, target):
        closet = root.val
        while root:
            closet = min(root.val, closet, key=lambda x:abs(x-target))
            root = root.left if target < root.val else root.right
        return closet
