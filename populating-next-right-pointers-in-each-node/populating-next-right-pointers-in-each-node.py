"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # method: bfs
        if not root:
            return root
        queue = deque()
        queue.append(root)
        
        
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                # default is null
                if i < level_size - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        # return root, not a list
        return root