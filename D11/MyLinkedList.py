class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        cur = self.head
        for i in range(index):
            if cur is None:
                return -1
            cur = cur.next
        if cur is None:
            return -1
        return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        cur = self.head
        temp = ListNode(val)
        temp.next = cur
        self.head = temp

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = ListNode(val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        cur = self.head
        if index == 0:
            self.addAtHead(val)
            return
        for i in range(index - 1):
            if cur is None:
                return
            cur = cur.next

        # while cur is not None and i<index-1:
        #     cur = cur.next
        #     i += 1
        if cur is None:
            return
        temp = ListNode(val)
        temp.next = cur.next
        cur.next = temp

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None

        """
        prev = None
        cur = self.head
        if index == 0:
            self.head = self.head.next
            return
        for i in range(index):
            if cur is None:
                return
            prev = cur
            cur = cur.next

        if prev.next is None:
            return
        prev.next = cur.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)