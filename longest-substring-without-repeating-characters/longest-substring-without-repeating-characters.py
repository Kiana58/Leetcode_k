class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # map format: mp[char] = idx
        mp = {}
        
        # two pointers:
        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            # if s[j] already in, move i
            if s[j] in mp:
                i = max(mp[s[j]], i)
            # update maximum length
            ans = max(ans, j - i + 1)
            # update idx in mp[s[j]] not matter in mp or not
            mp[s[j]] = j + 1

        return ans