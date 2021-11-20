class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
#         n = len(nums)
#         # binary search
#         # if n is odd, mid
#         l, r = 0, n-1
        
#         while l + 1 < r:
#             mid = (l + r)//2
#             if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
#                 return nums[mid]
#             elif nums[mid] == nums[mid+1]:
#                 l = mid
#             elif nums[mid-1] == nums[mid]:
#                 r = mid
#             else:
#                 r = mid
                
#         if nums[l-1] != nums[l] != nums[l+1]:
#             return nums[l]
#         if nums[r-1] != nums[r] != nums[r+1]:
#             return nums[r]
        
        lo, hi = 0, len(nums)-2  # hi starts from an even index so that hi^1 gives the next odd number
        while lo <= hi:
            mid = lo+(hi-lo)//2
            if nums[mid] == nums[mid^1]:
                lo = mid+1
            else:
                hi = mid-1
        return nums[lo]