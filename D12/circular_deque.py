class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.deque = [None] * k
        self.front_pointer = 0
        self.last_pointer = 0


    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.deque[self.front_pointer] is None:
            self.deque[self.front_pointer] = value
            return True
        previous = (self.front_pointer - 1 +len(self.deque) ) % len(self.deque)
        if self.deque[previous] is None:
            self.front_pointer = previous
            self.deque[self.front_pointer] = value
            return True
        return False


    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.deque[self.last_pointer] is None and self.front_pointer == self.last_pointer:
            self.deque[self.last_pointer] = value
            return True
        next_ptr = (self.last_pointer + 1) % len(self.deque)
        if self.deque[next_ptr] is None:
            self.last_pointer = next_ptr
            self.deque[self.last_pointer] = value
            return True
        return False

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.deque[self.front_pointer] is not None:
            self.deque[self.front_pointer] = None
            next_ptr = (self.front_pointer +1) % len(self.deque)
            if self.front_pointer == self.last_pointer:
                self.last_pointer = next_ptr
            self.front_pointer =next_ptr
            return True
        return False

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.deque[self.last_pointer] is not None:
            self.deque[self.last_pointer] = None
            previous = (self.last_pointer - 1) % len(self.deque)
            if self.front_pointer == self.last_pointer:
                self.front_pointer = previous
            self.last_pointer = previous
            return True
        return False

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        return self.deque[self.front_pointer]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        return self.deque[self.last_pointer]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        if self.last_pointer == self.front_pointer and self.deque[self.front_pointer] is None:
            return True
        return False

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        if self.deque[self.front_pointer - 1] is not None:
            return True
        return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()