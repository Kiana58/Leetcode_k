class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, n = 0, len(nums)
        while i < n:
            j = nums[i] - 1
            # why they are different?!!!!!
            # if nums[i] != nums[j] and 0 < nums[i] <= n:
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
                nums[i], nums[j] =  nums[j], nums[i]
            else:
                i += 1
        for idx in range(n):
            if nums[idx] != idx + 1:
                return idx+1
        return n + 1
        
