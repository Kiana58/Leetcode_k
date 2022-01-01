class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ##########################
        # method: if not based on num1, but generate new list res!!!!!, based on mock interview in pramp
        ##########################
#         i, j = 0, 0
#         res = []
#         nums1_m = nums1[:m]

#         while i < m or j < n:
#             # print(i, j)

#             # put j == m at first, so python eveluate it first, if not satisfied, not evaluate next condition
#             if j == n:
#                 res.append(nums1_m[i])
#                 i += 1   
#             elif i == m:
#                 res.append(nums2[j])
#                 j += 1    
#             elif nums1_m[i] <= nums2[j]:
#                 res.append(nums1_m[i])
#                 i += 1
#             # have to use elif, if use 'if', edge case problem        
#             elif nums1_m[i] > nums2[j]:
#                 res.append(nums2[j])
#                 j += 1
#             # print("res: ", res)
#         nums1 = res.copy()


#         # method: built in function

#         nums1[m:] = nums2
#         nums1.sort()
        
        # method: 3 pointers
        nums1_short = nums1[:m]
        
        p1, p2 = 0, 0
        
        for p in range(n+m):
            # if nums2 is run out or nums1 element is smaller
            # edge case: nums2 is empty, must put (p2>=n) at first
            if (p2 >= n) or (p1 < m and nums1_short[p1] <= nums2[p2]):
                nums1[p] = nums1_short[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1