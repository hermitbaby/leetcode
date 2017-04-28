# Given a binary tree, return the preorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        """
        observation:
        the order is the 'push element' order
        """
        stack = []
        output = []

        node = root
        while node or stack:
            if node:
                stack.append(node)
                output.append(node.val)
                node = node.left
            else:
                node = stack.pop()
                node = node.right

        return output



    def preOrder00(self, root):
        """
        how to store the result when in recursive function correctly?
        """
        if root == None:
            return []
        output = []
        output.append(root.val)

        if root.left:
            self.preOrder(root.left)
        if root.right:
            self.preOrder(root.right)

        return output


    def preOrder01(self, root):
        """
        """
        def preOrder(node):
            if node:
                # print node.val
                output.append(node.val)
                if node.left:
                    preOrder(node.left)
                if node.right:
                    preOrder(node.right)

        output = []
        preOrder(root)
        return output


    def init_btree(self):
        a = TreeNode('a')
        b = TreeNode('b')
        c = TreeNode('c')
        a.left = b
        a.right = c

        d = TreeNode('d')
        e = TreeNode('e')
        b.left = d
        b.right = e

        f = TreeNode('f')
        c.right = f

        print self.preOrder01(a)

    def init_btree2(self):
        a = TreeNode(1)
        b = TreeNode(2)
        c = TreeNode(3)

        a.right = b
        b.left = c
        print self.preorderTraversal(a)


    def init_btree3(self):
        a = TreeNode(1)
        b = TreeNode(2)
        c = TreeNode(3)

        a.right = b
        b.left = c
        print self.postorderTraversal(a)


    def postorderTraversal(self, root):
        parentStack = []
        lastVisitedNode = None
        output = []

        node = root
        while parentStack or node:
            if node:
                parentStack.append(node)
                # print parentStack
                node = node.left
                # print node.val if node else 'N/A'
            else:
                peekNode = parentStack[-1] if len(parentStack) > 0 else None
                # print parentStack[:]
                if peekNode.right != None and lastVisitedNode != peekNode.right:
                    node = peekNode.right
                else:
                    lastVisitedNode = parentStack.pop()
                    # print parentStack
                    output.append(lastVisitedNode.val)

        return output

s = Solution()
s.init_btree3()