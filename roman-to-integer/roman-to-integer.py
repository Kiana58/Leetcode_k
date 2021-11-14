class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        ans = 0
        
        for i in range(len(s)-1, -1, -1):
            num = roman[s[i]]
            # If a letter value is smaller than the last one seen, it should be subtracted.
            # In order to avoid declaring and using an an extra variable, we multiply numby any number between 2 and 4 before comparing it to ans, since the numerals jump in value by increments of at least 5x.
            if 4*num < ans:
                ans -= num
            else:
                ans += num
                
        return ans
        