class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Kiana solution 1: Brute Force
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
                    
        # Kiana solution 2: Using hashmap
        dic = {}
        for i, val in enumerate(nums):
            val_diff = target - val
            if val_diff in dic:
                return [dic[val_diff], i]
            else:
                dic[val] = i
        