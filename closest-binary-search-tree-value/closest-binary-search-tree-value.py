# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        upper = root
        lower = root
        
        while root:
            # if root < target, target is at right subtree
            if root.val < target:
                lower = root
                root = root.right
            elif root.val > target:
                upper = root
                root = root.left
            else:
                return root.val
            
        if_upper_closer = abs(upper.val - target) <= abs(lower.val - target)
        
        return upper.val if if_upper_closer else lower.val