# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, sum):

        def dfs( node, curSum, valList):
            if node.left == None and node.right == None:
                if curSum == sum:
                    result.append(valList)
            if node.left:
                dfs(node.left, curSum + node.left.val, valList + [node.left.val])
            if node.right:
                dfs(node.right, curSum + node.right.val, valList + [node.right.val])


        result = []
        if root == None:
            return []

        dfs(root, root.val, [root.val])
        return result

