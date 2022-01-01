class Solution:
    def isPalindrome(self, s: str) -> bool:
#         # method: built in function
#         filtered_chars = filter(lambda ch: ch.isalnum(), s)
#         lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

#         filtered_chars_list = list(lowercase_filtered_chars)
#         reversed_chars_list = filtered_chars_list[::-1]

#         return filtered_chars_list == reversed_chars_list

        # method: 2 pointers
        l, r = 0, len(s)-1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
            
        return True