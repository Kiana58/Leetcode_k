# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # method: for every node, find maximum left node path value and max right node path value
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
            
            # if gain is negative, ignore
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # for update new max_sum
            price_newpath = node.val + left_gain + right_gain
            max_sum = max(max_sum, price_newpath)
            
            # for recursion
            return node.val + max(left_gain, right_gain)
        
        max_sum = -math.inf
        max_gain(root)
        
        return max_sum
        