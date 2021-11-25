class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if len(nums) < 3:
            return math.inf
        
        res, diff_min = math.inf, math.inf
        for i in range(len(nums)):
            lo, hi = i+1, len(nums)-1
            
            while lo < hi:
                sum_3 = nums[i] + nums[lo] + nums[hi]
                diff = abs(sum_3 - target)
                if diff < diff_min:
                    diff_min = diff
                    res = sum_3
                    # print(res)

                if sum_3 < target:
                    lo += 1
                elif sum_3 > target:
                    hi -= 1
                else:
                    break
            
        return res

        
            