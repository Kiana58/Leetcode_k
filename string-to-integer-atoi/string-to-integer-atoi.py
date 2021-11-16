class Solution:
    def myAtoi(self, s: str) -> int:
        sign=""
		# check for and remove any leading whitespace
        if s.startswith(" "): s = s.lstrip()
		# to extract the sign before the number
        if s.startswith("-") or s.startswith("+"): 
            sign = s[0]
            s = s[1:]
        d=""
		# to extract just digits from the string
        for i in range(len(s)):
            if not s[i].isdigit(): break # edgecase for when there are characters before digits
            elif s[i].isdigit():
                d+=s[i]
                if i != len(s)-1: # edgecase for when there are only digits in the string
                    if not s[i+1].isdigit():  # to ignore the rest of the string if there are non-digit characters next
                        break
        if d == "": integer = 0 
        else: integer = int((sign+d))
        if integer < -2**31: integer = -2**31
        elif integer > 2**31 - 1: integer = 2**31-1
        return integer