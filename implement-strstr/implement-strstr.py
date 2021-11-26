class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # edge case 1
        if not needle:
            return 0
        # edge case 2, to avoid n-m = 0 below
        if haystack == needle:
            return 0
        
        n, m = len(haystack), len(needle)
        
        for idx in range(n-m+1):
            if haystack[idx:idx+m] == needle:
                return idx
        return -1