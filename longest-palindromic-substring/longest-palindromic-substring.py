class Solution:
    def longestPalindrome(self, s: str) -> str:
        # method: DP
#         length = len(s)
#         dp = {}
#         max_len = 1
#         start = 0
        
#         for _len in range(2, length+1):
#             i = 0
#             while i <= length - _len:
#                 j = i + _len - 1
#                 # base case: P(i, t) = true, P(i, i+1) = (Si == Si+1)
#                 # logic: P(i, i) = true, P(i,j)=(P(i+1,j−1) and Si==Sj)
#                 if (_len <= 3 and s[i] == s[j]) or (s[i] == s[j] and dp.get((i + 1, j - 1))):
#                     dp[(i, j)] = True
#                     if _len > max_len:
#                         max_len = _len
#                         start = i
#                 i += 1
#         return s[start:start + max_len]
        # method: expand from middle
        self.ans = ""
        self.ansLen = 0
        n = len(s)
        
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > self.ansLen:
                    self.ansLen = r-l+1
                    self.ans = s[l:r+1]
                l -= 1 
                r += 1
                    
        for i in range(n):
            # Odd Palindrom Strings
            expand(i, i)
                    
            # Even Palindrom Strings
            expand(i, i+1)
            
        return self.ans