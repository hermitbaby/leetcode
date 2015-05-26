# Given a binary tree, return the postorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [3,2,1].



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        parentStack = []
        lastVisitedNode = None
        output = []

        node = root
        while parentStack or node:
            if node:
                parentStack.append(node)
                node = node.left
            else:
                peekNode = parentStack[-1] if len(parentStack) > 0 else None
                if peekNode.right != None and lastVisitedNode != peekNode.right:
                    node = peekNode.right
                else:
                    lastVisitedNode = parentStack.pop()
                    output.append(lastVisitedNode.val)

        return output


