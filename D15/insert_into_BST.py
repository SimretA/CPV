# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            temp = TreeNode(val)
            return temp

        temp = root

        while temp is not None:
            if val > temp.val:
                if temp.right is None:
                    temp.right = TreeNode(val)
                    return root
                temp = temp.right

            else:
                if temp.left is None:
                    temp.left = TreeNode(val)
                    return root
                temp = temp.left


