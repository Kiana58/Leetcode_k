class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m, n = len(nums1), len(nums2)
        
        # print("nums1, nums2: ", nums1, nums2)
        
        # if (m+n) is a odd number
        mid_index = (m + n) //2
        # if (m+n) is a even number, mid_index - 1, mid_index
        
        # step 1: find mid_index in 2 sorted array
        # method: 2 pointer
        i, j, step = 0, 0, 0
        res = []
        while i < m or j < n:
            if j >= n:
                res.append(nums1[i])
                i += 1
            elif i >= m:
                res.append(nums2[j])
                j += 1
            elif nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
                
            if step == mid_index:
                # print('res: ', res)
                # print('step: ', step)
                break
            step += 1
        
        if m + n ==0:
            return None
        
        if m + n == 1:
            return res[-1]
            
        # print('res: ', res)
        
        if (m + n) % 2 != 0:
            return res.pop()
        else:
            return (res[-1] + res[-2])/2.0