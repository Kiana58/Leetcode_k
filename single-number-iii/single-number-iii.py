class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freqmap = {}
        for num in nums:
            if num not in freqmap:
                freqmap[num] = 0
            freqmap[num] += 1
        
        res = []
        for num in freqmap:
            if freqmap[num] == 1:
                res.append(num)
                
        return res
                