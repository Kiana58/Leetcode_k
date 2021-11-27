class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ##################
        # why this doest not work???
        ##################
#         if not nums:
#             return 0
#         idx = 0
#         while idx < len(nums):
#             while idx < len(nums) and nums[idx] != idx+1:
#                 if nums[idx] == nums[nums[idx]-1]:
#                     return nums[idx] 
#                 else:
#                     nums[idx], nums[nums[idx]-1] = nums[nums[idx]-1], nums[idx]
#             idx += 1
                
#         return nums[-1]

        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)