class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # base case, empty or not
        if not s:
            return s
        # initiate answer: (length of Palindromic, start position) which could transfer to (index start, index end) in s, put length first, because need max...
        answer = (0, 0)
        for mid in range(len(s)):
            # if Palindromeic len is odd
            answer = max(answer, self.get_Palindrome_from_mid(s, mid, mid))
            # if Palindromeic len is even
            answer = max(answer, self.get_Palindrome_from_mid(s, mid, mid+1))
            
        return s[answer[1]: answer[1]+answer[0]]
        
    def get_Palindrome_from_mid(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # from mid to both sides!!!
            left -= 1
            right += 1
        # length of Palindromic, start position
        return right - left - 1, left +1