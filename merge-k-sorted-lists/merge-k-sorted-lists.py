# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        # only works for Python 2, not Python 3 because __lt__ in class for node
        
        # method: using minHeap
        minHeap = []
        
        # initially put root in each linked list to minHeap
        for root in lists:
            if root:
                heappush(minHeap, (root.val, root))
                
        # create new linked list
        resultHead, resultTail = None, None
        while minHeap:
            # pop minimum value, append on the list
            val, node = heappop(minHeap)
            if not resultHead:
                resultHead = resultTail = node
            else:
                resultTail.next = node
                resultTail = resultTail.next
                
            # push node in the minHeap with size k
            if node.next:
                heappush(minHeap, (node.next.val, node.next))
                
        return resultHead