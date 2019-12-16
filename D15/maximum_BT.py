# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        max_index = 0
        if len(nums) < 1:
            return
        for i in range(1, len(nums)):
            if nums[max_index] < nums[i]:
                max_index = i
        temp = TreeNode(nums[max_index])
        temp.left = self.constructMaximumBinaryTree(nums[:max_index])
        temp.right = self.constructMaximumBinaryTree(nums[max_index + 1:])
        return temp
