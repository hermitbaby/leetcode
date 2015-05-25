#
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        if root == None:
            return []

        result = []
        nextLayer = [root]

        while len(nextLayer) > 0:
            result.append(nextLayer)

            nextLayer = []
            for father in result[-1]:
                if father.left:
                    nextLayer.append(father.left)
                if father.right:
                    nextLayer.append(father.right)

        result = [[ node.val for node in layer] for layer in result]

        #result = result[::-1]

        return result
