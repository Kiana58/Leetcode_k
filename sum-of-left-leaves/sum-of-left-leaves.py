# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, isLeft):
            if not node:
                return 0
            # if at leaf node
            if not node.left and not node.right:
                return node.val if isLeft else 0
            return dfs(node.left, True) + dfs(node.right, False)
        # why first is False???!!! because it is not leaf
        return dfs(root, False)

        
        