# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         # step 1: two points, n steps away , start at head
#         point, point_n = head, head
#         for _ in range(n):
#             if point_n.next:
#                 point_n = point_n.next
#             else:
#                 return None
        
#         # edge case: if length of linked list is n, return head.next
#         if point_n is None:
#             return point.next
#         # step 2: move 2nd point to end, then 1st point is nth node from the end. 
#         # stop when point_n is at end of linked list, find the point
#         while point_n.next:
#             point = point.next
#             point_n = point_n.next
            
#         # step 3: change the 1st point.next to remove the nth node
#         # if point.next is None:
#         #     point.next = None
#         # else:
#         point.next = point.next.next
        
#         return head
    
    
        fast = slow = head
        for i in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head