class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        !!!!! Kiana example: 12587 -> 12758, find next bigger number
        """
        
        i = j = len(nums)-1
        # find 1st element nums[i-1] < nums[i]
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        # if could not find, means nums is always descending, like 321, no next bigger number, just reverse
        if i == 0: 
            nums.reverse()
            return 
        # k is last ascending position, then always descending at i
        k = i - 1  
        # find first element from end of nums which is > nums[k], 
        # since always descending, so it is the next bigger element than nums[k] in 2nd part
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]  
        # reverse the part from i to end: always decending part for ordering
        l, r = k+1, len(nums)-1 
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1
        
        # !!! no need to return, since change on nums
        
        
