# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = None
        temp = None
        carry = 0
        if l1 is not None and l2 is not None:
            added = l1.val + l2.val + carry
            carry = added // 10
            result = ListNode(added % 10)
            temp = result
            l1 = l1.next
            l2 = l2.next
            while l1 is not None and l2 is not None:
                added = l1.val + l2.val + carry
                carry = added // 10
                temp.next = ListNode(added % 10)
                temp = temp.next
                l1 = l1.next
                l2 = l2.next
            while l1 is not None:
                added = l1.val + carry
                carry = added // 10
                temp.next = ListNode(added % 10)
                temp = temp.next
                l1 = l1.next
            while l2 is not None:
                added = l2.val + carry
                carry = added // 10
                temp.next = ListNode(added % 10)
                temp = temp.next
                l2 = l2.next
            if carry != 0:
                temp.next = ListNode(carry)
                temp = temp.next
        elif l1 is not None:
            result = l1
        elif l2 is not None:
            result = l2
        return result