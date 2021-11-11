class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # # start with first sum_v > 1
        # start = 1
        # sum_v = 0
        # for num in nums:
        #     sum_v += num
        #     while sum_v + num < 1:
        #         start += 1
        #         sum_v += 1
        # return start
        
        # return -min(0, min(accumulate(nums))) + 1
        
        Sum, ans = 0, 0
        for el in nums:
            Sum = Sum + el
            ans = min(ans, Sum)
        return -ans + 1