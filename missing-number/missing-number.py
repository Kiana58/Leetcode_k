class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # method: math
        sum_nums, n = 0, len(nums)
        for num in nums:
            sum_nums += num
            
        # integer: using //2 
        return n*(n+1)//2 - sum_nums