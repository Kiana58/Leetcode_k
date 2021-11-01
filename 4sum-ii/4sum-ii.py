class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        counter = {}
        for a in nums1:
            for b in nums2:
                counter[a+b] = counter.get(a+b, 0) + 1
        answer = 0
        for c in nums3:
            for d in nums4:
                answer += counter.get(-c-d, 0)
        return answer