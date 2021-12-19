class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        l = 0 
        r = 0 
        while l < len(nums) and r <len(nums):
            # find the location when the number starts to be different. 
            # compare num at l and r 
            while r<len(nums) and nums[l]==nums[r]:
                r+=1
            if l+1<len(nums) and r<len(nums):
                nums[l+1]=nums[r]
                l+=1
        return l+1

