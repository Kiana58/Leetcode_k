# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # edge case:
        if not head:
            return None
        # find last element & length of linked list
        last_node = head
        l = 1
        while last_node.next:
            last_node = last_node.next
            l += 1

        k = k % l

        # move last_node to 1st node
        last_node.next = head
        # find the node as new last_node
        tempNode = head
        for _ in range( l - k - 1 ):
            tempNode = tempNode.next

        new_last = tempNode.next
        tempNode.next = None


        return new_last
