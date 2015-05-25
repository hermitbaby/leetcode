# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric0(self, root):
        if root == None:
            return True
        else:
            return self.isSym(root.left, root.right)


    def isSym(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        elif left.val != right.val:
            return False
        else:
            return self.isSym(left.left, right.right) and \
                self.isSym(left.right, right.left)



    def isSymmetric(self, root):
        if root == None:
            return True

        stack = [[root.left, root.right]]

        while len(stack) > 0:
            left, right = stack.pop()

            if left == None and right == None:
                continue
            if left == None or right == None:
                return False
            if left.val == right.val:
                stack.append([left.left, right.right])
                stack.append([left.right, right.left])
            else:
                return False
        return True