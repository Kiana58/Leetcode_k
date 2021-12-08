class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # edge case
        if not s or not t:
            return ""
        
        # sliding window method:
        l, r = 0, 0
        # dict for t, each char: counts
        dict_t = Counter(t)
        # num of unique characters in t
        required = len(dict_t)
        
        # num of unique characters in current window
        formed = 0
        # dict for current window: char and counts
        window_cnts = {}
        
        # ans: tuple of window length, left, right
        ans = float("inf"), None, None
        
        
        while r < len(s):
            # add right char to the window dic
            char = s[r]
            window_cnts[char] = window_cnts.get(char, 0) + 1
            # if current char in t and freq  == to the one in t, then formed += 1
            if char in dict_t and window_cnts[char] == dict_t[char]:
                formed += 1
            # contract window from left for condition
            while l <= r and formed == required:
                char = s[l]
                window_cnts[char] -= 1
                if char in dict_t and window_cnts[char] < dict_t[char]:
                    formed -= 1
                # save smallest window
                if r - l + 1 < ans[0]:
                    ans = (r-l+1, l, r)

                l += 1

            r += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
    
            