# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        return self.add(root, L, R)

    def add(self, root, L, R):
        if root is None:
            return 0
        left = root.left
        right = root.right
        if L <= root.val <= R:
            return root.val + self.add(left, L, R) + self.add(right, L, R)
        else:
            return self.add(left, L, R) + self.add(right, L, R)