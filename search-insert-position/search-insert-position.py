class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        
        if nums[lo] > target:
            return lo
        
        if nums[hi] < target:
            return hi + 1
        
        while lo + 1 < hi:
            mid = (lo + hi)//2
            
            if nums[mid] < target:
                lo = mid
            elif nums[mid] > target:
                hi = mid
            else:
                return mid
            
        # return lo
        if nums[lo] == target:
            return lo   
        if nums[hi] == target:
            return hi
        
        if nums[lo] < target and nums[hi] > target:
            return lo+1
        
        
        if nums[hi] < target:
            return hi + 1