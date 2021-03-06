# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # if empty
        if not root:
            return None
        
        if root == p or root == q:
            return root
        
        # find in left or right subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # if find one in left subtree, the other in right subtree
        if left and right:
            return root
        
        # if both in left subtree
        if left:
            return left
        
        # if both in right subtree
        if right:
            return right
        
        # if neither in left or right
        return None