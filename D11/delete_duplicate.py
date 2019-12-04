#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        nextNode = None
        while cur is not None:
            nextNode = cur.next
            if (nextNode is None):
                return head
            if cur.val == nextNode.val:
                cur.next = nextNode.next
            else:
                cur = nextNode
        return head
