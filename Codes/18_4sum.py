class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        # !!!! use set to avoid duplicates
        result = set()
        # !!!! edge case: not exists
        k = 4
        if len(nums) == 0 or nums[0]* k > target or nums[-1] * k < target:
            return list(result)
        # !!! edge case: all num in nums are same !!!! nums[-1] == nums[0]
        temp = []
        if len(nums) >= k and nums[0] == nums[-1]:
            if nums[0] * k == target:
                while k > 0:
                    temp.append(nums[0])
                    k -= 1
                result.add(tuple(temp))
            return list(result)

        
        for i in range(n-3):
            # skip if duplicated nums to avoid duplicates
            # !!!! index is tricky
            # !!! edge case: all num in nums are same !!!! nums[-1] == nums[0]
            # if nums[i] == nums[i-1]:
            #     continue
            for j in range(i+1, n-2):
                # if nums[j] == nums[j-1]:
                #     continue
                # 2 pointer
                l, r = j+1, n-1
                while l < r:
                    sum_4 = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum_4 == target:
                        # because result is a set, add tuple !!!!
                        result.add(tuple([nums[i], nums[j], nums[l], nums[r]]))
                        # do not forgot to update index !!!
                        l += 1
                        r -= 1
                        # while l < r and nums[l] == nums[l-1]:
                        #     l += 1
                        # while l < r and nums[r] == nums[r+1]:
                        #     r -= 1
                    elif sum_4 < target:
                        l += 1
                    else:
                        r -= 1
        result = list(result)
        return result

# # using generalized Nsum to get 4sum!!!
#     def fourSum(self, nums, target):
#         nums.sort()
#         results = []
#         self.findNsum(nums, target, 4, [], results)
#         return results

#     def findNsum(self, nums, target, N, result, results):
#         if len(nums) < N or N < 2: return

#         # solve 2-sum
#         if N == 2:
#             l,r = 0,len(nums)-1
#             while l < r:
#                 if nums[l] + nums[r] == target:
#                     results.append(result + [nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#                     while l < r and nums[l] == nums[l - 1]:
#                         l += 1
#                     while r > l and nums[r] == nums[r + 1]:
#                         r -= 1
#                 elif nums[l] + nums[r] < target:
#                     l += 1
#                 else:
#                     r -= 1
#         else:
#             for i in range(0, len(nums)-N+1):   # careful about range
#                 if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
#                     break
#                 if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
#                     self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
#         return

                        
        
