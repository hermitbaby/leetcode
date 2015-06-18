# -*- coding: UTF-8 -*-
#                             1
#
# 　　　　　　　　　　　　　　　/　  \
#
# 　　　　　　　　　　　　　　 2       3
#
# 　　　　　　　　　　　　　 /    \    /   \
#
# 　　　　　　　　　　　　　4     5  6    7


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def preorder(self, root, level, res):
        if root:
            # print res
            if len(res) < level+1:
                res.append([])
            res[level].append(root.val)
            self.preorder(root.left, level+1, res)
            self.preorder(root.right, level+1, res)

    def levelOrder(self, root):
        res=[]
        self.preorder(root, 0, res)
        return res


    def preorder2(self, root, level, res):
        if root:
            print res
            if len(res) < level+1:
                res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)

            self.preorder2(root.left, level+1, res)
            self.preorder2(root.right, level+1, res)

    def zigzagLevelOrder(self, root):
        res=[]
        self.preorder2(root, 0, res)
        return res



s = Solution()

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

# print s.levelOrder(n1)

print s.zigzagLevelOrder(n1)
