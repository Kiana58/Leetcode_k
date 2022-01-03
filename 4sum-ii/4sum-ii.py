class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # # method 1: using built function counter.get()
        # counter = {}
        # for a in nums1:
        #     for b in nums2:
        #         counter[a+b] = counter.get(a+b, 0) + 1
        # answer = 0
        # for c in nums3:
        #     for d in nums4:
        #         answer += counter.get(-c-d, 0)
        # return answer
        
        # method 2: count k list
        def nSumCount(lists: List[List[int]]) -> int:
            addToHash(lists, 0, 0)
            return countComplements(lists, len(lists) // 2, 0)

        def addToHash(lists: List[List[int]], i: int, sum: int) -> None:
            # we will divide k arrays into two groups. For the first group, we will have k/2 nested loops to count sums. Another k/2 nested loops will enumerate arrays in the second group and search for complements.
            if i == len(lists) // 2:
                m[sum] = m.get(sum, 0) + 1
            else:
                for a in lists[i]:
                    addToHash(lists, i + 1, sum + a)

        def countComplements(lists: List[List[int]], i: int, complement: int) -> int:
            if i == len(lists):
                return m.get(complement, 0)
            cnt = 0
            for a in lists[i]:
                cnt += countComplements(lists, i + 1, complement - a)
            return cnt

        m = {}
        return nSumCount([nums1, nums2, nums3, nums4])