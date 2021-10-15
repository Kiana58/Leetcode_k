# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        """
        Kiana notes: Given preorder (current, left, right) --> root, each level, ...
        """
        if not preorder:
            return None
        # Since preorder, 1st is always the root
        root = TreeNode(preorder[0])
        i = 1
        # get 1st node from left side which is for right sub tree, all nodes >= root, 
        while i < len(preorder) and preorder[i] < root.val:
            i += 1
        # recursive left & right subtree
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
