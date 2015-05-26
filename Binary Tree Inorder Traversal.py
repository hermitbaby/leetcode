# Given a binary tree, return the inorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].
#
# Note: Recursive solution is trivial, could you do it iteratively?
#
#



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        """
        observation:
        the order is the 'pop element' order
        """
        # parentStack, store parent node info
        stack = []
        output = []

        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                output.append(node.val)
                node = node.right

        return output