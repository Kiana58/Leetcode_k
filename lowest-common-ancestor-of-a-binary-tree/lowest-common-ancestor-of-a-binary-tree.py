# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # method: if both in left or right tree, then return p or q; if not, return root
        # #######################
        # High-Level Approach #
        #######################
        # If both nodes are in the tree, vanilla search for both nodes eventually succeeds.

        def recursive_dfs(root, n1, n2, result):
            # edge case
            if not root:
                return False, False # n1_found, n2_found
            n1_eq_curr, n2_eq_curr = n1 == root, n2 == root
            
            n1_in_l, n2_in_l = recursive_dfs(root.left, n1, n2, result)
            n1_in_r, n2_in_r = recursive_dfs(root.right, n1, n2, result)
            
            n1_found = n1_eq_curr or n1_in_l or n1_in_r
            n2_found = n2_eq_curr or n2_in_l or n2_in_r
            both_found = n1_found and n2_found
            if both_found:
                result.append(root)
            return n1_found, n2_found
        result = []
        recursive_dfs(root, p, q, result)
        return result[0] if result else None # handles p or q not in root