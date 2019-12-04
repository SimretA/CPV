from D11.Node import Node


class LinkedList:
    def __init__(self):
        self.node = None

    def add_node(self, node):
        if self.node is None:
            self.node = node
        else:
            last = self.node
            while last.next is not None:
                last = last.next
            last.next = node

    def delete_node(self, data):
        previous = None
        cur = self.node
        while cur.data != data:
            previous = cur
            cur = cur.next
        previous.next = cur.next

    def exists(self, data):
        cur = self.node
        while cur.next is not None:
            if cur.data == data:
                return True
            cur = cur.next
        if cur.data == data:
            return True
        return False

    def print_ll(self):
        cur = self.node
        while cur.next is not None:
            print(cur.data, end=" --> ")
            cur = cur.next
        print(cur.data)


if __name__ == '__main__':
    linked_list = LinkedList()
    node1 = Node(2)
    linked_list.add_node(node1)
    linked_list.print_ll()
    node2 = Node(5)
    linked_list.add_node(node2)
    linked_list.print_ll()

    linked_list.add_node(Node(100))
    linked_list.add_node(Node(9))
    linked_list.add_node(Node(3))
    linked_list.print_ll()
    linked_list.delete_node(100)
    linked_list.print_ll()
    print(linked_list.exists(3))
