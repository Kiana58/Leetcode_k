# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
#         # if use path, wrong...why????!!!!
#         def dfs(node, path):
#             nonlocal results
#             if node:
#                 path.append(str(node.val))
#                 # if at the leaf node
#                 if not node.left and not node.right:
#                     path_num = int(''.join(path))
#                     print('path_num: ', path_num)
#                     results += path_num
#                     # path = []
#                 if node.left:
#                     dfs(node.left, path)
#                 if node.right:
#                     dfs(node.right, path)
        
#         results = 0
#         dfs(root, [])
        
#         return results
    
        def dfs(node, sum_s):
            nonlocal results
            if node:
                sum_s = sum_s*10 + node.val
                # if at the leaf node
                if not node.left and not node.right:
                    results += sum_s
                if node.left:
                    dfs(node.left, sum_s)
                if node.right:
                    dfs(node.right, sum_s)
        
        results = 0
        dfs(root, 0)
        
        return results