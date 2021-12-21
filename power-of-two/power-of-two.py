class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        # edge case
        if n == 0:
            return False
        
        # method: recursion
        while n % 2 == 0:
            n /= 2
        
        return n == 1

            