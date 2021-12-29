class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # method: binary search
        """
        mid before k: target < nums[mid] or ow
        mid after k: target > nums[mid] or ow
        """
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            # check mid is before ratated k or after
            if nums[mid] >= nums[start]: # before k
                # !!! have to add target >= nums[start] 
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else: # after k
                # !!! have to add target <= nums[end]
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
                    
        return -1
                    
    
        