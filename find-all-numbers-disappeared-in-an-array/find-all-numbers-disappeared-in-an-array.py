class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # solution without extra space
        # put the value as same range as idx
        nums = [num - 1 for num in nums]
        n = len(nums)
        idx = 0
        for idx, num in enumerate(nums):
            curr_num = num
            while curr_num != idx and nums[curr_num] != curr_num:
                nums[idx], nums[curr_num] = nums[curr_num], nums[idx]
                curr_num = nums[idx]
                
        res = []
        
        for idx, num in enumerate(nums):
            if idx != num:
                res.append(idx+1)
                
        return res
        