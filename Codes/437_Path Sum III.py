from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        # define global result and path
        self.result = 0
        cache = {0:1}
        
        # recursive to get result
        self.dfs_preorder(root, targetSum, 0, cache)
        
        # return result
        return self.result
    
    
    """
    create a dictionary (named cache) which saves all the path sum (from root to current node) and their frequency. Again, we traverse through the tree, at each node, we can get the currPathSum (from root to current node). If within this path, there is a valid solution, then there must be a oldPathSum such that currPathSum - oldPathSum = target.
We just need to add the frequency of the oldPathSum to the result.
During the DFS break down, we need to -1 in cache[currPathSum], because this path is not available in later traverse.
Check the graph below for easy visualization.
    """
    def dfs_preorder(self, node, targetSum, curr_sum, cache):
        # if node is empty
        if not node:
            return

        curr_sum += node.val
        oldPathSum = curr_sum - targetSum
        
        # update result and cache
        # if the path from root
        self.result += cache.get(oldPathSum, 0)
        cache[curr_sum] = cache.get(curr_sum, 0) + 1

        # recurisive left and right tree
        self.dfs_preorder(node.left, targetSum, curr_sum, cache)
        self.dfs_preorder(node.right, targetSum, curr_sum, cache)

        # !!!!!! remove ????
        cache[curr_sum] -= 1
    
