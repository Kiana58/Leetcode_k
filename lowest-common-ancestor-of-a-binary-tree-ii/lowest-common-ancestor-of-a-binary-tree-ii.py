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
        p_exist, q_exist, lca = self.helper(root, p, q)
        return lca if p_exist and q_exist else None
    
    def helper(self, root, p, q):
        # base/edge case
        if not root:
            return False, False, None
        
        
        # recurisive, left and right subtree
        left_p_exist, left_q_exist, left_node = self.helper(root.left, p, q)
        right_p_exist, right_q_exist, right_node = self.helper(root.right, p, q)
        
        # calculate p_exist and q_exist
        p_exist = left_p_exist or right_p_exist or root == p
        q_exist = left_q_exist or right_q_exist or root == q
        
        # if p or q is at root
        if root == p or root == q:
            return p_exist, q_exist, root
        
        # if p is in one subtree and q is in another subtree
        if left_node and right_node:
            return p_exist, q_exist, root
        
        # if only in left subtree
        if left_node:
            return p_exist, q_exist, left_node
        # if only in right subtree
        if right_node:
            return p_exist, q_exist, right_node
        # if in neither of subtrees
        return p_exist, q_exist, None
        