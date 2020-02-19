# https://leetcode.com/problems/linked-list-cycle/submissions/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #         my_dict = {}
        #         while head != None:
        #             if head in my_dict:
        #                 return True
        #             else:
        #                 my_dict[head] = 1
        #             head = head.next

        #         return False

        if head is None or head.next is None:
            return False

        slow, fast = head, head.next

        while slow != fast:
            if fast == None or fast.next == None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True