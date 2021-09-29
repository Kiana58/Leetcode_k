class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        index_lst = []
        
        # freqmap for p
        freqmap = {}
        for char in p:
            if char not in freqmap:
                freqmap[char] = 0
            freqmap[char] += 1
            
        n, m = len(s), len(p)
        # initialize freqmap_s for s_s
        s_s = s[0:m]
        # freqmap for s_s
        freqmap_s = {}
        for char in s_s:
            if char not in freqmap_s:
                freqmap_s[char] = 0
            freqmap_s[char] += 1
        if freqmap_s == freqmap:
            index_lst.append(0)
        
        # range to n, because end index
        for i in range(m,n):
            char_end = s[i]
            if char_end not in freqmap_s:
                freqmap_s[char_end] = 0
            freqmap_s[char_end] += 1
            char_before = s[i-m]
            freqmap_s[char_before] -= 1
            if freqmap_s[char_before] == 0:
                del freqmap_s[char_before]
            if freqmap_s == freqmap:
                # append start index
                index_lst.append(i-m+1)
                
        return index_lst
        
