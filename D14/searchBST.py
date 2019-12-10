# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        self.recursive_search(root, val)

    def recursive_search(self, node, val):

        if node.val == val:
            return node
        left = node.left
        right = node.right
        if left is not None and right is not None:
            print("node.left")
            return
        elif node.left is None:
            self.recursive_search(node.right, val)
        elif node.right is None:
            self.recursive_search(node.left, val)
        else:
            left = node.left
            right = node.right
            self.recursive_search(left, val)
            self.recursive_search(right, val)


