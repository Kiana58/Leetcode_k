class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # method: 2 arrays, left & right, then left * right
        left, right, n = [], [], len(nums)
        l_prod, r_prod = 1, 1
        
        for i in range(n):
            # first append, since the element on the left
            left.append(l_prod)
            l_prod *= nums[i]
            
        for i in range(n-1, -1, -1):
            # first append, since the element on the right
            right.append(r_prod)
            r_prod *= nums[i]
            
        right.reverse()
        res = [l * r for l, r in zip(left, right)]
        return res