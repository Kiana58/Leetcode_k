class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n, m = len(s2), len(s1)
        
        # freq map for s1
        freqmap = {}
        for s in s1:
            if s not in freqmap:
                freqmap[s] = 0
            freqmap[s] += 1
            
        # go through s2
        for i in range(n-m+1):
            s2_s = s2[i:i+m]
            freqmap_s2s = {}
            for s in s2_s:
                if s not in freqmap_s2s:
                    freqmap_s2s[s] = 0
                freqmap_s2s[s] += 1
            if freqmap_s2s == freqmap:
                return True
            
        return False
