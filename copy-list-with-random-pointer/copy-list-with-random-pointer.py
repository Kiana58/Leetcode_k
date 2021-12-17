"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        if head in self.visitedHash:
            return self.visitedHash[head]
        
        node = Node(head.val)
        self.visitedHash[head] = node
        
        # recurision
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node