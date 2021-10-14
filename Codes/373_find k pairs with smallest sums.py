class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        maxHeap = []
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                num1, num2 = nums1[i], nums2[j]
                num_sum = num1+num2
                heappush(maxHeap, (-num_sum, num1, num2))
                if len(maxHeap) > k:
                    num_sum_neg_p, num1_p, num2_p = heappop(maxHeap)
                    if  -num_sum < num_sum_neg_p:
                        break
        result = [(num1, num2) for (num_sum_neg, num1, num2) in maxHeap]
        return result
