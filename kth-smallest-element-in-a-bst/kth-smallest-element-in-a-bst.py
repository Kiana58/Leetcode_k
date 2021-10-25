# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # because BST, so in order dfs, smallest to largest
        stack = []
        
        # put all left most nodes in stack
        while root:
            stack.append(root)
            root = root.left
        
        # for k-1 times, then put kth smallest at the top of stack
        for i in range(k-1):
            node = stack.pop()
            # if have right subtree, put left most nodes of right subtree in stack
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
                    
        return stack[-1].val