# Given a binary tree, return the inorder traversal of its nodes' values.
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?

class Node():
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

class Solution():
    def inorder_traveral_recur(self, root):
        res = []
        if root == None:
            return res

        if root != None:
            res = self.inorder_traveral(root.left)
            res.append(root.value)
            res += self.inorder_traveral(root.right)
        return res

    def inorder_traversal_iter(self, root):
        res = []
        stack = []
        cur = root
        while cur != None or len(stack) != 0:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.value)
            cur = cur.right
        return res