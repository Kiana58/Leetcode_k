# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        if not root or k == 0:
            return []
        
        # from tree to list, ordered from left to right
        nums = self.get_inorder(root)
        # find the index which are near the target, then use two pointer from that
        left = self.find_lower_index(nums, target)
        right = left + 1
        results = []
        for _ in range(k):
            if self.is_left_closer(nums, left, right, target):
                results.append(nums[left])
                left -= 1
            else:
                results.append(nums[right])
                right += 1
        return results
    
    def get_inorder(self, root):
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        inorder = []
        
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                # find most left leaf
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                inorder.append(stack[-1].val)
                
        return inorder
    
    # binary search to find left index
    def find_lower_index(self, nums, target):
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = (start + end)//2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
                
        if nums[end] < target:
            return end
        if nums[start] < target:
            return start
        return -1
    
    def is_left_closer(self, nums, left, right, target):
        if left < 0:
            return False
        if right >= len(nums):
            return True
        return target - nums[left] < nums[right] - target
        