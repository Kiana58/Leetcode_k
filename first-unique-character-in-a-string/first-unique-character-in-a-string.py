class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqmap = {}
        
        for s1 in s:
            if s1 not in freqmap:
                freqmap[s1] = 0
            freqmap[s1] += 1
        
        idx = 0
        for s1 in s:
            if freqmap[s1] == 1:
                return idx
            idx += 1
            
        return -1