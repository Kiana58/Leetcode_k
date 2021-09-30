# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1 or head is None:
            return head
        
        pre, curr = None, head
        
        # reverse every k group:
        while True:
            i = 0
            lastG_last = pre
            currG_last = curr
            next = None
            # if kth_curr is None, last part < k:
            # use k-1 from current, not k from pre(None)!!! 
            # tricky, otherwise if size of linkedlist is k, kth_curr is none
            kth_curr = self.get_kth(curr, k-1)
            if not kth_curr:
                break
            while i < k and curr:
                temp = curr.next
                curr.next = pre
                pre = curr
                curr = temp
                i += 1
            # connect with lastG if not 1stG
            if lastG_last:
                lastG_last.next = pre
            else:
                head = pre
                
            # connect with nextG
            currG_last.next = curr
            if curr is None:
                break
                
            pre = currG_last
            
        return head
            
        
    def get_kth(self, curr, k):
        while k > 0 and curr:
            curr = curr.next
            k -= 1
        return curr
