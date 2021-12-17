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
        # reverse part
        def reverseH(node, k):
            pre, curr = None, node
            # for every K nodes
            while k:
                curr.next, pre, curr = pre, curr, curr.next
                k -= 1
                
            return pre
        
        # count length of linked list, is it less than k
        cnt = 0
        tail = head
        while cnt < k and tail:
            tail = tail.next
            cnt += 1
            
        # if k nodes:
        if cnt == k:
            revHead = reverseH(head, k)
            
            # recurision
            head.next = self.reverseKGroup(tail, k)
            return revHead
        
        return head