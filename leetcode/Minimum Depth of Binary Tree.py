# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        elif root.left == None:
            return 1 + self.minDepth(root.right)
        elif root.right == None:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


    def minDepth0(self, root):
        if root == None:
            return 0

        stack = []
        stack.append([root, 1])

        while len(stack) > 0:
            node, depth = stack.pop()

            if node.left:
                stack.append([root.left, depth+1])
            if node.right:
                stack.append([root.right, depth+1])

            if node.left == None and node.right == None:
                return depth

        return 0