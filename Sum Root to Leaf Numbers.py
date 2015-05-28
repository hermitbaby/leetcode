# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# For example,
#
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
# Return the sum = 12 + 13 = 25.



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        def sum(node, preSum):
            if node == None:
                return 0
            preSum = preSum * 10 + node.val
            if node.left == None and node.right == None:
                return preSum
            return sum(node.left, preSum) + sum(node.right, preSum)

        node = root
        return sum(node, 0)