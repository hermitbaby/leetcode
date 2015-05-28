# Given a binary tree
#
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Note:
#
# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
# For example,
#
# Given the following perfect binary tree,
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL



# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect0(self, root):
        """
        handle perfect binary tree
        """
        node = root

        if node and node.left:
            node.left.next = node.right

            if node.next:
                # if parent node has next
                node.right.next = node.next.left
            else:
                # if parent node don't has next
                node.right.next = None

            self.connect(node.left)
            self.connect(node.right)



    def connect(self, root):
        pass




# Follow up for problem "Populating Next Right Pointers in Each Node".
#
# What if the given tree could be any binary tree? Would your previous solution still work?
#
# Note:
#
# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL


    def connect(self, root):
        fatherLayerCurrent = root
        sonLayerHead = None
        sonLayerCurrent = None

        # Travel layer by layer as BFS travesal.
        while fatherLayerCurrent != None:
            # Travel inside a layer from left to right
            while fatherLayerCurrent != None:
                # Try to access the left son if there is
                if fatherLayerCurrent.left != None:
                    if sonLayerHead == None:
                        sonLayerHead = fatherLayerCurrent.left
                        sonLayerCurrent = sonLayerHead
                    else:
                        sonLayerCurrent.next = fatherLayerCurrent.left
                        sonLayerCurrent = sonLayerCurrent.next

                # Try to access the right son if there is
                if fatherLayerCurrent.right != None:
                    if sonLayerHead == None:
                        sonLayerHead = fatherLayerCurrent.right
                        sonLayerCurrent = sonLayerHead
                    else:
                        sonLayerCurrent.next = fatherLayerCurrent.right
                        sonLayerCurrent = sonLayerCurrent.next

                fatherLayerCurrent = fatherLayerCurrent.next

            # Prepare to move down to the next layer.
            fatherLayerCurrent = sonLayerHead
            sonLayerHead =None

        return