"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
#         cnt = 0
#         while cnt < n:
#             length = read4(buf)
#             cnt += length
#             if length < 4:
#                 break

#         return min(n, cnt)
    
    
        tmp = [" "] * 4
        ans = []
        cnt = 0
        while cnt < n:
            length = read4(tmp)
            ans += tmp[:length]
            cnt += length
            if length < 4:
                break
        buf[:n] = ans
        return min(n, cnt)