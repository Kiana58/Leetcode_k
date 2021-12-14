# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # step1: transfer linkedlist to num, then add
        def to_num(l1):
            res = []
            if not l1:
                return 0
            tail = l1
            while tail:
                res.append(str(tail.val))
                tail = tail.next
                
            res.reverse()
            res_str = ''.join(res)
            print(res_str)
            return int(res_str)
        
        res_num = to_num(l1) + to_num(l2)
        
        # step2: transfer num to linked list
        res_num_lst = [int(num) for num in str(res_num)]
        res_num_lst.reverse()
        
        head = ListNode(res_num_lst[0])
        node = head
        for i in range(1, len(res_num_lst)):
            node.next = ListNode(res_num_lst[i])
            node = node.next
        
        return head
                
        