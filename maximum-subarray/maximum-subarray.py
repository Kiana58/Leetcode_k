class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_max = sum_curr = nums[0]
        
        for num in nums[1:]:
            # if sum_curr < 0, ignore
            sum_curr = max(num, sum_curr + num)
            sum_max = max(sum_max, sum_curr)
            
        return sum_max