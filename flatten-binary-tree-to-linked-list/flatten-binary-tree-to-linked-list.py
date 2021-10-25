# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # dfs preorder, then link always by right child
        self.flatten_return_last_node(root)
        
    def flatten_return_last_node(self, root):
        # if empty
        if not root:
            return None
        
        # left and right subtree recursive
        left_last = self.flatten_return_last_node(root.left)
        right_last = self.flatten_return_last_node(root.right)
        
        # if left subtree is not empty, assign root, flattened left subtree then right subtree
        if left_last:
            # left subtree + right subtree
            left_last.right = root.right
            # root + left subtree
            root.right = root.left
            # left child pointer is always null
            root.left = None
        # if left subtree is empty, not need to assign, root.right is right subtree
        
        # return last not of flattened tree
        return right_last or left_last or root
        
            