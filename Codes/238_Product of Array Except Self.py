class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # !!!! L to save all product of elements on the left side of element i
        L, R = [1], [1]
        prod_L, prod_R = 1, 1
        n = len(nums)
        for i in range(n-1):
            prod_L *= nums[i]
            L.append(prod_L)
            
        for i in range(n-1, 0, -1):
            prod_R *= nums[i]
            R.append(prod_R)
        # !!!! reverse
        R.reverse()
        
        res = [L[i] * R[i] for i in range(n)]
        
        return res
            
