class Solution:
    def maxPower(self, s: str) -> int:
        n = len(s)
        # both are started at 1, not 0 !!!!!!!
        # to count the duplicates
        cnt = 1
        # to record the max count
        power = 1
        
        for i in range(1, n):
            if s[i] != s[i-1]:
                cnt = 1
            else:
                cnt += 1
                power = max(power, cnt)
                
        return power