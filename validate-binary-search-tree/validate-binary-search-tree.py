# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

#         if root.left:
#             if root.left.val >= root.val:
#                 return False
#             else:
#                 self.isValidBST(root.left)

#         if root.right:
#             if root.right.val <= root.val:
#                 return False
#             else:
#                 self.isValidBST(root.right)

        # validate each node.val, not node.val between leftnode and right node val!!!
        def validate(node, low=-math.inf, high=math.inf):
            # empty tree is a valid BST
            if not node:
                return True 
            if node.val <= low or node.val >= high:
                return False
            
            return (validate(node.right, node.val, high) and validate(node.left, low, node.val))
                
        return validate(root)
            