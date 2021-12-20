# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        # method: bfs
        # bfs using queue
        queue = deque()
        queue.append(root)
        
        if not root:
            return res
        
        while queue:
            level_size = len(queue)
            curr_level = []
            for _ in range(level_size):
                # pop left from queue for current level
                node = queue.popleft()
                curr_level.append(node.val)
                # add left or right node to queue if available!!!
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # current level finished, append to result
            res.append(curr_level)
            
            
        return res
            