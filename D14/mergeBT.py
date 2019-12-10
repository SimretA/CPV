# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return self.addNode(t1, t2)

    def addNode(self, node1, node2):
        if node1 is not None and node2 is not None:
            temp = TreeNode(node1.val + node2.val)
            temp.right = self.addNode(node1.right, node2.right)
            temp.left = self.addNode(node1.left, node2.left)
        elif node1 is not None:
            temp = TreeNode(node1.val)
            temp.right = self.addNode(node1.right, None)
            temp.left = self.addNode(node1.left, None)
        elif node2 is not None:
            temp = TreeNode(node2.val)
            temp.right = self.addNode(None, node2.right)
            temp.left = self.addNode(None, node2.left)
        else:
            return

        return temp

