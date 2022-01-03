class Solution:
    def validPalindrome(self, s: str) -> bool:
#         # edge case
#         if s == s[::-1]:
#             return True
        
#         l, r = 0, len(s)-1
#         while l < r:
#             if s[l] != s[r]:
#                 del_left = s[:l] + s[l+1:]
#                 del_right = s[:r] + s[r+1:]
#                 return (del_left == del_left[::-1]) or (del_right == del_right[::-1])
#             l -= 1
#             r += 1

        if s == s[::-1]:
            return True
        
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                del_left = s[:left] + s[left+1:]
                del_right = s[:right] + s[right+1:]
                if del_left == del_left[::-1] or del_right == del_right[::-1]:
                    return True
                else:
                    return False
            
            left += 1
            right -= 1