# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # pre: create a dummy node, no need to create nxt
        pre, curr = None, head
        
        if not head:
            return None
        
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
            
        return pre