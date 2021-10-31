class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        def fastpow(num, p):
            if p == 0:
                return 1
            temp = fastpow(num,p//2)
            if (p % 2):
                return temp*temp*num
            else:
                return temp*temp
        
        
        num, p = x, n
        if n < 0:
            num = 1/x
            p = -n
            
        
        return fastpow(num,p)
        