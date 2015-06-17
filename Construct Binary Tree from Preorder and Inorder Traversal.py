# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}

    # def buildTree(self, preorder, inorder):
    #     if len(preorder) == 0:
    #         return None
    #     if len(preorder) == 1:
    #         return TreeNode(preorder[0])
    #     root = TreeNode(preorder[0])
    #     index = inorder.index(root.val)
    #     root.left = self.buildTree(preorder[1 : index + 1], inorder[0 : index])
    #     root.right = self.buildTree(preorder[index + 1 : len(preorder)], inorder[index + 1 : len(inorder)])
    #     return root
    def buildTree(self, preorder, inorder):
        if not inorder: return None # inorder is empty
        self.inorder, self.preorder = inorder, preorder
        return self.dfs(0, 0, len(inorder))

    def dfs(self, inLeft, preLeft, Len):
        if Len <= 0:
            return None
        root = TreeNode(self.preorder[preLeft])
        rootPos = self.inorder.index(root.val)
        print rootPos, inLeft, preLeft+1
        root.left = self.dfs(inLeft, preLeft+1, rootPos - inLeft)
        root.right = self.dfs(rootPos + 1, preLeft + rootPos - inLeft, Len - 1 - (rootPos - inLeft))
        return root


s = Solution()
preorder = [1,2,4,5, 3,6,7]
inorder = [4,2,5,1,6,3,7]
s.buildTree(preorder, inorder)

