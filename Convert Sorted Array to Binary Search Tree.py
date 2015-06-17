# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        return self.createBST(nums, 0, len(nums)-1)

    def createBST(self, nums, start, end):
        if start > end:
            return
        mid = (start + end) /2
        root = TreeNode(nums[mid])
        root.left = self.createBST(nums, start, mid -1)
        root.right = self.createBST(nums, mid+1, end)
        return root

