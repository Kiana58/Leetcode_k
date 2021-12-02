# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case: empty or just one node
        if not head or not head.next:
            return head
        
        # step 1: even head record
        even_head = head.next
        
        # step 2: odd linked list and even linked list moving forward
        odd, even = head, head.next
        
        while odd.next and odd.next.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
            
        # step 3: connect odd linked list tail to even_head
        odd.next = even_head
        
        return head
        