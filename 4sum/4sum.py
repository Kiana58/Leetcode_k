class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def ksum(nums, target, k):
            res = []
            # edge case
            if not nums:
                return res
            
            avg = target // k
            
            # edge case
            if avg < nums[0] or nums[-1] < avg:
                return res
    
            if k == 2:
                return twoSum(nums, target)
            
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in ksum(nums[i+1:], target - nums[i], k - 1):
                        res.append([nums[i]]+subset)
            return res
        
        def twoSum(nums, target):
            # use two pointer
            lo, hi = 0, len(nums)-1
            res = []

            while lo < hi:
                sum_2 = nums[lo] + nums[hi]

                if sum_2 < target:
                    lo += 1
                elif sum_2 > target:
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
            return res
                    
                    
        nums.sort()
            
        return ksum(nums, target, 4)