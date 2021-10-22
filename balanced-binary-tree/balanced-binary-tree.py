# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        is_balanced, _ = self.DivideC(root)
        return is_balanced
    
    # return balanced or not, height of tree for node
    def DivideC(self, node):
        if not node:
            return True, 0
        
        # D & C
        is_left_balanced, left_height = self.DivideC(node.left)
        is_right_balanced, right_height = self.DivideC(node.right)
        root_height = max(left_height, right_height) + 1
        
        # decision
        # if left tree is not balanced or right is not
        if not is_left_balanced or not is_right_balanced:
            return False, root_height
        
        # balanced tree definition
        if abs(left_height - right_height) >1:
            return False, root_height
        
        return True, root_height
        