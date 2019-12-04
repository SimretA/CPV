# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        listNode = None
        nextNode = None
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                temp = ListNode(l1.val)
                if listNode is None:
                    listNode = temp
                    nextNode = listNode
                else:
                    nextNode.next = temp
                    nextNode = nextNode.next
                l1 = l1.next
            else:
                temp = ListNode(l2.val)
                if listNode is None:
                    listNode = temp
                    nextNode = listNode
                else:
                    nextNode.next = temp
                    nextNode = nextNode.next
                l2 = l2.next
        while l1 is not None:
            temp = ListNode(l1.val)
            if listNode is None:
                listNode = temp
                nextNode = listNode
            else:
                nextNode.next = temp
                nextNode = nextNode.next
            l1 = l1.next
        while l2 is not None:
            temp = ListNode(l2.val)
            if listNode is None:
                listNode = temp
                nextNode = listNode
            else:
                nextNode.next = temp
                nextNode = nextNode.next
            l2 = l2.next
        return listNode

