class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # using double pointer
        # freqmap for every element in s
        counter = {}
        answer = 0
        j = 0
        # max_freq for one element
        max_freq = 0
        
        for i in range(len(s)):
            # max_freq means max_freq for element at s[i:j], but global value to compare
            # while satisfy condition for k
            while j < len(s) and j - i - max_freq <= k:
                counter[s[j]] = counter.get(s[j], 0) +1
                max_freq = max(max_freq, counter[s[j]])
                j += 1
                
            # update answer
            if j - i - max_freq > k:
                answer = max(answer, j-1-i)
            else:
                answer = max(answer, j-i)
                
            # update max_freq
            counter[s[i]] -= 1
            max_freq = max(counter.values())
            
        return answer
            
            
                