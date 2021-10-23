class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
#         p0 = curr = 0
#         # for all idx > p2 : nums[idx > p2] = 2
#         p2 = len(nums) - 1

#         while curr <= p2:
#             if nums[curr] == 0:
#                 nums[p0], nums[curr] = nums[curr], nums[p0]
#                 p0 += 1
#                 curr += 1
#             elif nums[curr] == 2:
#                 nums[curr], nums[p2] = nums[p2], nums[curr]
#                 p2 -= 1
#             else:
#                 curr += 1
        if not nums:
            return
        
        # method which is in O(N), not O(nlogN) as above
        # # freqmap to record cnts
        # color_cnts = {}
        # for num in nums:
        #     if num not in color_cnts:
        #         color_cnts[num] = 0
        #     color_cnts[num] += 1
        
        # if use list not dic, color 0, 1, 2 as the idx of list
        color_cnts = [0]*3
        for num in nums:
            color_cnts[num] += 1
            
        # fill the nums according to freqmap
        idx = 0
        for i in range(len(color_cnts)):
            cnt = color_cnts[i]
            while cnt > 0:
                nums[idx] = i
                cnt -= 1
                idx += 1
        return nums   