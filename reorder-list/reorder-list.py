# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        # step 1: find the middle of linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # step 2: reverse 2nd part of the list
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
            
        # step 3: merge two sorted linked list
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next