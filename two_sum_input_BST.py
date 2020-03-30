# Given a Binary Search Tree and a target number, return true if there exist two elements
# in the BST such that their sum is equal to the given target.

# Example 1:
#
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 9
#
# Output: True

# Example 2:
#
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 28
#
# Output: False

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def find_target(self, root, k):
        res = []
        self.inorder(root, res)
        i, j = 0, len(res)-1
        while i < j:
            total = res[i] + res[j]
            if total == k:
                return True
            elif total < k:
                i += 1
            else:
                j -= 1
        return False

    def inorder(self, root, res=[]):
        if root:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)





